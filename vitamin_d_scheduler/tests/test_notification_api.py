"""Test scheduler notification API"""

from datetime import datetime, timedelta


def test_create_notification_schedule(flask_client):
    """Test create notification schedule"""
    data = {
            'user_id': 1,
            'message': 'Test message',
            'notification_date': datetime.now() + timedelta(hours=1).
    }
    response = flask_client.post('/api/notification/create', data=data)

    assert isinstance(response.data, bytes)
