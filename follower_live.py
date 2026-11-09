import os
import scratchattach as sa

USERNAME = os.environ["SCRATCH_USERNAME"]
PASSWORD = os.environ["SCRATCH_PASSWORD"]
PROJECT_ID = "1437662848"

print("Scratchにログイン中...")

session = sa.login(USERNAME, PASSWORD)

print("Scratchに接続成功！")

user = session.connect_user(USERNAME)
count = user.follower_count()

print(f"現在のフォロワー数: {count}")

cloud = session.connect_cloud(PROJECT_ID)
cloud.set_var("followers", str(count))

print("Scratchに送信成功！")
