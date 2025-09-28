import asyncio
import aiohttp
import os
from mcp.server import Server
from mcp.server.models import InitializationOptions
from mcp.server.lowlevel import NotificationOptions
import mcp.server.stdio
import mcp.types as types

server = Server("wathq-server")

# API key for Wathq (using the Consumer Key as the API key)
api_key = os.getenv("WATHQ_API_KEY")

async def get_national_cr_number(session, headers, reg_number):
    """Get national CR number from regular CR number"""
    if reg_number.startswith("700"):
        # Already a national CR number
        return reg_number
    else:
        # Regular CR number - get national CR number
        national_cr_url = f"https://api.wathq.sa/commercial-registration/crNationalNumber/{reg_number}"
        
        async with session.get(national_cr_url, headers=headers) as response:
            data = await response.json()
            
            if 'crNationalNumber' in data:
                return data['crNationalNumber']
            else:
                raise Exception(f"Could not get national CR number: {data}")

async def get_company_info(session, headers, reg_number):
    """Get company information by CR number or national CR number"""
    national_cr_number = await get_national_cr_number(session, headers, reg_number)
    
    # Use national CR number for fullinfo endpoint
    url = f"https://api.wathq.sa/commercial-registration/fullinfo/{national_cr_number}?language=en"
    
    async with session.get(url, headers=headers) as response:
        return await response.json()

async def get_company_contract(session, headers, reg_number):
    """Get company contract/articles of association by CR number or national CR number"""
    national_cr_number = await get_national_cr_number(session, headers, reg_number)
    
    # Use national CR number for contract endpoint
    url = f"https://api.wathq.sa/company-contract/info/{national_cr_number}?language=en"
    
    async with session.get(url, headers=headers) as response:
        return await response.json()

async def get_national_address(session, headers, reg_number):
    """Get national address information by CR number or national CR number"""
    
    # Use national CR number for address endpoint
    url = f"https://api.wathq.sa/spl/national/address/info/{reg_number}"
    
    async with session.get(url, headers=headers) as response:
        return await response.json()

async def get_real_estate_deed(session, headers, deed_number, id_number, id_type):
    """Get real estate deed details"""
    url = f"https://api.wathq.sa/moj/real-estate/deed/{deed_number}/{id_number}/{id_type}"
    
    async with session.get(url, headers=headers) as response:
        return await response.json()

async def get_attorney_info(session, headers, attorney_code):
    """Get attorney information details"""
    url = f"https://api.wathq.sa/v1/attorney/info/{attorney_code}"
    
    async with session.get(url, headers=headers) as response:
        return await response.json()

@server.list_tools()
async def handle_list_tools() -> list[types.Tool]:
    return [
        types.Tool(
            name="lookup_company",
            description="Look up Saudi company information by CR number or national CR number",
            inputSchema={
                "type": "object",
                "properties": {
                    "registration_number": {
                        "type": "string",
                        "description": "The company registration number (CR number or national CR number)"
                    }
                },
                "required": ["registration_number"]
            }
        ),
        types.Tool(
            name="lookup_company_contract",
            description="Get company articles of association and contract details",
            inputSchema={
                "type": "object",
                "properties": {
                    "registration_number": {
                        "type": "string",
                        "description": "The company registration number (CR number or national CR number)"
                    }
                },
                "required": ["registration_number"]
            }
        ),
        types.Tool(
            name="lookup_national_address",
            description="Get national address information for establishment",
            inputSchema={
                "type": "object",
                "properties": {
                    "registration_number": {
                        "type": "string",
                        "description": "The company registration number (CR number or national CR number)"
                    }
                },
                "required": ["registration_number"]
            }
        ),
        types.Tool(
            name="lookup_real_estate_deed",
            description="Get real estate deed details",
            inputSchema={
                "type": "object",
                "properties": {
                    "deed_number": {
                        "type": "string",
                        "description": "The real estate deed number"
                    },
                    "id_number": {
                        "type": "string",
                        "description": "The ID number (national ID, CR number, etc.)"
                    },
                    "id_type": {
                        "type": "string",
                        "description": "The type of ID (1=National ID, 2=CR Number, etc.)"
                    }
                },
                "required": ["deed_number", "id_number", "id_type"]
            }
        ),
        types.Tool(
            name="lookup_attorney_info",
            description="Verify attorney information details",
            inputSchema={
                "type": "object",
                "properties": {
                    "attorney_code": {
                        "type": "string",
                        "description": "The attorney code"
                    }
                },
                "required": ["attorney_code"]
            }
        ),
        types.Tool(
            name="lookup_employee",
            description="Look up employee information by national ID",
            inputSchema={
                "type": "object",
                "properties": {
                    "national_id": {
                        "type": "string",
                        "description": "The employee's national ID number"
                    }
                },
                "required": ["national_id"]
            }
        )
    ]

@server.call_tool()
async def handle_call_tool(name: str, arguments: dict) -> list[types.TextContent]:
    if not api_key:
        return [types.TextContent(
            type="text",
            text="Error: WATHQ_API_KEY environment variable not set"
        )]
    
    async with aiohttp.ClientSession() as session:
        headers = {
            "apiKey": api_key,
            "Accept": "application/json"
        }
        
        if name == "lookup_company":
            reg_number = arguments["registration_number"]
            data = await get_company_info(session, headers, reg_number)
            return [types.TextContent(type="text", text=str(data))]
            
        elif name == "lookup_company_contract":
            reg_number = arguments["registration_number"]
            data = await get_company_contract(session, headers, reg_number)
            return [types.TextContent(type="text", text=str(data))]
            
        elif name == "lookup_national_address":
            reg_number = arguments["registration_number"]
            data = await get_national_address(session, headers, reg_number)
            return [types.TextContent(type="text", text=str(data))]
            
        elif name == "lookup_real_estate_deed":
            deed_number = arguments["deed_number"]
            id_number = arguments["id_number"]
            id_type = arguments["id_type"]
            data = await get_real_estate_deed(session, headers, deed_number, id_number, id_type)
            return [types.TextContent(type="text", text=str(data))]
            
        elif name == "lookup_attorney_info":
            attorney_code = arguments["attorney_code"]
            data = await get_attorney_info(session, headers, attorney_code)
            return [types.TextContent(type="text", text=str(data))]
            
        elif name == "lookup_employee":
            national_id = arguments["national_id"]
            url = f"https://api.wathq.sa/masdr/employee/info/{national_id}"
            
            async with session.get(url, headers=headers) as response:
                data = await response.json()
                return [types.TextContent(type="text", text=str(data))]

async def main():
    async with mcp.server.stdio.stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            InitializationOptions(
                server_name="wathq-server",
                server_version="0.1.0",
                capabilities=server.get_capabilities(
                    notification_options=NotificationOptions(),
                    experimental_capabilities={}
                )
            )
        )

if __name__ == "__main__":
    asyncio.run(main())
