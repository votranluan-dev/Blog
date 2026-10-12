from database import SessionLocal
from model import Post

with SessionLocal() as db:
    post = db.get(Post, 3)

    if post:
        db.delete(post)
        db.commit()
        print("Đã xóa Post ID 3")
    else:
        print("Không tìm thấy Post ID 3")