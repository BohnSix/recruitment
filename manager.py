from recruitment.app.init import app

app.debug = True
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5001)
