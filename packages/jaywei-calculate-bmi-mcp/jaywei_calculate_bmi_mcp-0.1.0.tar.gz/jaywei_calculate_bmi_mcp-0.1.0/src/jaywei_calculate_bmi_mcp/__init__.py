from mcp.server.fastmcp import FastMCP

mcp = FastMCP("calculate_bmi_mcp_stdio")

@mcp.tool()
def calculate_bmi(weight_kg:float,height_m:float)->float:
    """通过给定的体重和身高计算 BMI 指数。

    Args:
        weight_kg (float): 用户的体重，单位为公斤 (kg)。
        height_m (float): 用户的身高，单位为米 (m)。

    Returns:
        float: 计算得出的 BMI 指数值。
    """
    return weight_kg / (height_m ** 2)

def main() -> None:
    mcp.run(transport="stdio")