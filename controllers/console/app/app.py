import uuid

from flask_restful import Resource, reqparse, inputs
from werkzeug.exceptions import abort

# 允许创建的应用类型
ALLOW_CREATE_APP_MODES = ['chat', 'agent-chat', 'advanced-chat', 'workflow', 'completion']


class AppListApi(Resource):
    """获取应用列表"""

    def get(self):
        def uuid_list(value):
            try:
                return [str(uuid.UUID(v)) for v in value.split(',')]
            except ValueError:
                abort(400, message="Invalid UUID format in tag_ids")

        parser = reqparse.RequestParser()
        parser.add_argument('page', type=inputs.int_range(1, 99999), required=False, default=1, location='args')
        parser.add_argument('limit', type=inputs.int_range(1, 100), required=False, default=20, location='args')
        parser.add_argument('mode', type=str, choices=['chat', 'workflow', 'agent-chat', 'channel', 'all'],
                            default='all', location='args', required=False)
        parser.add_argument('name', type=str, location='args', required=False)
        parser.add_argument('tag_ids', type=uuid_list, location='args', required=False)

        args = parser.parse_args()

        app_service=AppService()
