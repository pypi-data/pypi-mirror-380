from .core import (
    MissingEnvVarsError, VarSpec, EnvSpec,
    load_env, require_vars, setup_logging,
)

from .decorators import (
    retry, timer,
)

from .utils import (
    safe_get, print_table,
    write_json, read_json, append_json_line, pretty_print_json,
    slugify, camel_to_snake, snake_to_camel,
    normalize_whitespace, remove_html_tags,
    extract_emails, extract_urls,
)



__version__ = "0.4.0"
__all__ = [
    "safe_get",
    "print_table",
    "write_json", "read_json", "append_json_line", "pretty_print_json",
    "atomic_write_text", "atomic_write_json",
    "iter_json_lines", "read_json_lines", "tail_json_lines",
    "count_file_lines", "merge_json_files", "validate_json",
    "slugify", "camel_to_snake", "snake_to_camel",
    "normalize_whitespace", "remove_html_tags",
    "extract_emails", "extract_urls",
]