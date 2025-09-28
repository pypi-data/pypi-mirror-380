import os
from collections import Counter, defaultdict
from copy import deepcopy
from functools import partial

from spaghettree import Result, safe
from spaghettree.domain.entities import EntityCST, ImportCST, ImportType
from spaghettree.domain.optimisation import (
    AdjMat,
    merge_single_entity_communities_if_no_gain_penalty,
    optimise_communities,
)
from spaghettree.domain.parsing import (
    cst_to_str,
    pair_exclusive_calls,
)
from spaghettree.domain.visitors import EntityLocation
from spaghettree.logger import logger


def optimise_entity_positions(
    entities: dict[str, EntityCST],
    location_map: dict[str, EntityLocation],
    call_tree: dict[str, list[str]],
    src_root: str,
    new_root: str,
) -> Result:
    return (
        AdjMat.from_call_tree(call_tree, optimise=True)
        .and_then(pair_exclusive_calls)
        .and_then(optimise_communities)
        .and_then(merge_single_entity_communities_if_no_gain_penalty)
        .and_then(partial(create_new_module_map, entities=entities))
        .and_then(infer_module_names)
        .and_then(rename_overlapping_mod_names)
        .and_then(remap_imports)
        .and_then(
            partial(
                convert_to_code_str,
                order_map=location_map,
            ),
        )
        .and_then(partial(create_new_filepaths, new_root=new_root or src_root))
        .and_then(add_empty_inits_if_needed)
    )


@safe
def create_new_module_map(
    adj_mat: AdjMat,
    entities: dict[str, EntityCST],
) -> dict[int, list[EntityCST]]:
    new_modules: defaultdict[int, list[EntityCST]] = defaultdict(list)

    for i, mod_name in enumerate(adj_mat.communities):
        ent_name = adj_mat.node_map[i]
        new_modules[mod_name].append(entities[ent_name])

    return dict(new_modules)


@safe
def infer_module_names(
    new_modules: dict[int, list[EntityCST]],
) -> dict[str, list[EntityCST]]:
    logger.debug(f"{new_modules = }")

    renamed_modules: dict[str, list[EntityCST]] = defaultdict(list)

    for contents in new_modules.values():
        logger.debug(f"{contents = }")
        if len(contents) > 1:
            names = [".".join(ent.name.split(".")[:-1]) for ent in contents]
            possible_module_names = sorted(
                {(name, names.count(name)) for name in names}, key=lambda x: (-x[1], x[0])
            )
            logger.debug(f"{possible_module_names = }")

            for name, _ in possible_module_names:
                if name not in renamed_modules:
                    mod_name = name
                    break
            else:
                mod_name = f"{possible_module_names[0][0]}.mod_overflow"
        else:
            mod_name = contents[0].name
        logger.debug(f"{mod_name = }")
        renamed_modules[mod_name].extend(contents)

    logger.debug(f"{renamed_modules = }")
    return dict(renamed_modules)


@safe
def rename_overlapping_mod_names(
    renamed_modules: dict[str, list[EntityCST]],
) -> dict[str, list[EntityCST]]:
    def rename_mod_name(name: str, renamed_modules: list[str]) -> str:
        logger.debug(f"{name = }")
        name_parts = name.split(".")
        root = name_parts[0]
        dirname = ".".join(name_parts[:-1])
        basename = name_parts[-1]

        dirnames = [".".join(m.split(".")[:-1]) for m in renamed_modules]
        dirname_counts = Counter(dirnames)

        logger.debug(f"{dirname_counts = }")

        if (basename in ("__all__", "logger") and dirname.endswith(".__init__")) or (
            dirname not in renamed_modules and dirname_counts.get(dirname, 0) <= 1
        ):
            name = dirname
        elif dirname in renamed_modules:
            name = ".".join([*name_parts[:-2], "_".join(name_parts[-2:])])

        if "." not in name:
            name = f"{root}.{name}"
        logger.debug(f"{name = }")
        return name.lower()

    mod_names = list(renamed_modules)
    logger.debug(f"{renamed_modules = }")
    logger.debug(f"{mod_names = }")
    return {
        rename_mod_name(name, mod_names): contents for name, contents in renamed_modules.items()
    }


@safe
def remap_imports(
    modules: dict[str, list[EntityCST]],
) -> dict[str, list[EntityCST]]:
    logger.debug(f"{modules = }")

    modules = deepcopy(modules)
    entity_mod_map: dict[str, str] = {
        ent.name: mod_name for mod_name, ents in modules.items() for ent in ents
    }

    for mod_name, ents in modules.items():
        for ent in ents:
            updated_imports: set[ImportCST] = set()

            for imp in ent.imports:
                new_mod = entity_mod_map.get(f"{imp.module}.{imp.name}")
                if new_mod is None:
                    updated_imports.add(imp)
                elif new_mod != mod_name:
                    updated_imports.add(
                        ImportCST(
                            module=new_mod,
                            import_type=imp.import_type,
                            name=imp.name,
                            as_name=imp.as_name,
                        ),
                    )
            updated_imports.add(
                ImportCST(
                    module="__future__",
                    import_type=ImportType.FROM,
                    name="annotations",
                    as_name="annotations",
                )
            )
            ent.imports = updated_imports
            logger.debug(f"{mod_name = } {ent = }")
    return modules


@safe
def create_new_filepaths(
    fixed_name_modules: dict[str, list[EntityCST]],
    new_root: str,
) -> dict[str, list[EntityCST]]:
    logger.debug(f"{fixed_name_modules = }")

    def to_filepath(new_root: str, name: str) -> str:
        return os.path.join(os.path.dirname(new_root), name.replace(".", "/") + ".py")

    return {to_filepath(new_root, name): contents for name, contents in fixed_name_modules.items()}


@safe
def convert_to_code_str(
    new_modules: dict[str, list[EntityCST]],
    order_map: dict[str, int],
) -> dict[str, str]:
    logger.debug(f"{new_modules = }")
    logger.debug(f"{order_map = }")

    def get_module_str(mod_contents: list[EntityCST]) -> str:
        imports, code = [], []

        for ent in mod_contents:
            imports.extend([imp.to_str() for imp in ent.imports])
            code.append(cst_to_str(ent.tree))

        return "".join(sorted(set(imports))) + "\n".join(code)

    return {
        mod_name: get_module_str(sorted(contents, key=lambda x: order_map[x.name.split(".")[-1]]))
        for mod_name, contents in new_modules.items()
    }


@safe
def add_empty_inits_if_needed(modules: dict[str, str]) -> dict[str, str]:
    logger.debug(f"{modules = }")

    modules_with_inits = {}

    for path, contents in modules.items():
        init_path = f"{os.path.dirname(path)}/__init__.py"

        if init_path not in modules and init_path not in modules_with_inits:
            logger.debug(f"creating __init__ {init_path = }")
            modules_with_inits[init_path] = ""

        if not contents.strip() and os.path.basename(path) != "__init__.py":
            logger.debug(f"Skipping {path = } {contents = }")
            # skip empty files
            continue
        logger.debug(f"{path = } {contents = }")
        modules_with_inits[path] = contents

    return modules_with_inits
