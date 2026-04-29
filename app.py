import boto3
from flask import Flask, request, jsonify
from botocore.exceptions import ClientError
import os

app = Flask(__name__)

# הגדרת החיבור ל-DynamoDB
# בקוברנטיס, הוא יזהה אוטומטית את ההרשאות מהמכונה (אם נגדיר אותן בטראפורם)
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('weather_history')

@app.route('/track', methods=['POST'])
def track():
    data = request.json
    city = data.get('city')
    
    if not city:
        return jsonify({"error": "City is required"}), 400

    try:
        # עדכון המונה: אם העיר קיימת - תוסיף 1, אם לא - תיצור אותה עם 1
        table.update_item(
            Key={'search_id': city},
            UpdateExpression="ADD search_count :inc",
            ExpressionAttributeValues={':inc': 1}
        )
        return jsonify({"status": "tracked", "city": city}), 200
    except ClientError as e:
        return jsonify({"error": e.response['Error']['Message']}), 500

@app.route('/stats', methods=['GET'])
def get_stats():
    try:
        response = table.scan()
        items = response.get('Items', [])
        # הופך את הרשימה למילון של עיר: כמות
        stats = {item['search_id']: int(item['search_count']) for item in items}
        return jsonify(stats)
    except ClientError as e:
        return jsonify({"error": e.response['Error']['Message']}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)