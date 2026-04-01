"""
极简HTTP服务器
"""
from http.server import HTTPServer, BaseHTTPRequestHandler
import sqlite3
import json

class SimpleAPI(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/api/v1/travels":
            # 从数据库获取所有旅行数据
            data = self.get_all_travels()

            self.send_response(200)
            # 添加 CORS 头
            self.send_header("Access-Control-Allow-Origin", "*")
            self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
            self.send_header("Access-Control-Allow-Headers", "Content-Type")
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(data).encode('utf-8'))

        elif self.path.startswith("/api/v1/travels/"):
            # 获取slug
            slug = self.path.split("/")[-1]
            
            # 从数据库获取单个旅行数据
            data = self.get_travel_by_slug(slug)

            self.send_response(200)
            # 添加 CORS 头
            self.send_header("Access-Control-Allow-Origin", "*")
            self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
            self.send_header("Access-Control-Allow-Headers", "Content-Type")
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(data).encode('utf-8'))

        else:
            self.send_error(404)
    
    def get_all_travels(self):
        """从数据库获取所有旅行数据"""
        conn = sqlite3.connect('travels.db')
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        cursor.execute('SELECT * FROM travels')
        rows = cursor.fetchall()
        
        data = []
        for row in rows:
            travel = {
                "id": row["id"],
                "title": row["title"],
                "slug": row["slug"],
                "visual_hook": row["visual_hook"],
                "content_story": row["content_story"],
                "cover_url": row["cover_url"],
                "gallery_urls": json.loads(row["gallery_urls"]) if row["gallery_urls"] else [],
                "experience_type": row["experience_type"],
                "visual_style": row["visual_style"],
                "rarity_level": row["rarity_level"],
                "emotional_tone": row["emotional_tone"]
            }
            data.append(travel)
        
        conn.close()
        return data
    
    def get_travel_by_slug(self, slug):
        """根据slug从数据库获取单个旅行数据"""
        conn = sqlite3.connect('travels.db')
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        cursor.execute('SELECT * FROM travels WHERE slug = ?', (slug,))
        row = cursor.fetchone()
        
        if row:
            travel = {
                "id": row["id"],
                "title": row["title"],
                "slug": row["slug"],
                "visual_hook": row["visual_hook"],
                "content_story": row["content_story"],
                "cover_url": row["cover_url"],
                "gallery_urls": json.loads(row["gallery_urls"]) if row["gallery_urls"] else [],
                "experience_type": row["experience_type"],
                "visual_style": row["visual_style"],
                "rarity_level": row["rarity_level"],
                "emotional_tone": row["emotional_tone"]
            }
        else:
            # 如果没有找到对应的数据，返回默认数据
            cursor.execute('SELECT * FROM travels LIMIT 1')
            row = cursor.fetchone()
            if row:
                travel = {
                    "id": row["id"],
                    "title": row["title"],
                    "slug": row["slug"],
                    "visual_hook": row["visual_hook"],
                    "content_story": row["content_story"],
                    "cover_url": row["cover_url"],
                    "gallery_urls": json.loads(row["gallery_urls"]) if row["gallery_urls"] else [],
                    "experience_type": row["experience_type"],
                    "visual_style": row["visual_style"],
                    "rarity_level": row["rarity_level"],
                    "emotional_tone": row["emotional_tone"]
                }
            else:
                # 如果数据库为空，返回一个默认的空对象
                travel = {}
        
        conn.close()
        return travel

def run():
    server = HTTPServer(("localhost", 8000), SimpleAPI)
    print("Server started on port 8000")
    server.serve_forever()

if __name__ == "__main__":
    run()