import os
import scratchattach as sa

USERNAME = os.environ["SCRATCH_USERNAME"]
PASSWORD = os.environ["SCRATCH_PASSWORD"]
PROJECT_ID = "1437662848"

cloud = None

try:
    print("Scratchにログイン中...", flush=True)

    session = sa.login(USERNAME, PASSWORD)

    print("Scratchに接続成功！", flush=True)

    user = session.connect_user(USERNAME)
    count = user.follower_count()

    print(f"現在のフォロワー数: {count}", flush=True)

    cloud = session.connect_cloud(PROJECT_ID)

    print("送信前:", cloud.get_var("followers"), flush=True)

    cloud.set_var("followers", str(count))

    print("送信処理完了！", flush=True)

finally:
    if cloud is not None:
        cloud.disconnect()
        print("Scratchとの接続を終了しました！", flush=True)

print("すべての処理が完了しました！", flush=True)
