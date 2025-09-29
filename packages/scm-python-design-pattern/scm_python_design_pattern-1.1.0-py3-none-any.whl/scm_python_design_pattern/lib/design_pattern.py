import tapps.code.designPattern as code_design_pattern
from tio.tcli import cli_invoker, OptParser

flags = [
    ("n:", "name=", "short name", "design_pattern/design-pattern"),
    ("p:", "package=", "package", "design_pattern/design-pattern"),
]

opp = OptParser(flags)


@cli_invoker("design_pattern/design-pattern")  # 设计模式生成类
def code_design_pattern_handler(package: str, name: str):
    code_design_pattern.entrypoint_code_design_pattern_handler(package, name)
