import json

from models.enums.app_mode import AppMode

default_app_templates = {
    # 工作流默认模板
    AppMode.WORKFLOW: {
        'app': {
            'mode': AppMode.WORKFLOW.value,
            'enable_site': True,
            'enable_api': True
        }
    },

    AppMode.COMPLETION: {
        'app': {
            'mode': AppMode.COMPLETION.value,
            'enable_site': True,
            'enable_api': True
        },
        'model_config': {
            'model': {
                "provider": "openai",
                "name": "gpt-4",
                "mode": "chat",
                "completion_params": {}
            },
            'user_input_from': json.dumps([
                {
                    "paragraph": {
                        "label": "Query",
                        "variable": "query",
                        "required": True,
                        "default": ""
                    }
                }
            ]),
            'pre_prompt': '{{query}}'
        },
    },

    # 聊天应用默认模板
    AppMode.CHAT: {
        'app': {
            'mode': AppMode.CHAT.value,
            'enable_site': True,
            'enable_api': True
        },
        'model_config': {
            'model': {
                "provider": "openai",
                "name": "gpt-4",
                "mode": "chat",
                "completion_params": {}
            }
        }
    },

    # advance-chat 默认模板
    AppMode.ADVANCED_CHAT:{
        'app':{
            'mode': AppMode.ADVANCED_CHAT.value,
            'enable_site': True,
            'enable_api': True
        }
    },

    # agent_chat 默认模板
    AppMode.AGENT_CHAT:{
        'app':{
            'mode': AppMode.AGENT_CHAT.value,
            'enable_site': True,
            'enable_api': True
        },
        'model_config': {
            'model':{
                "provider": "openai",
                "name": "gpt-4",
                "mode": "chat",
                "completion_params": {}
            }
        }
    }

}
