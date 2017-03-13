from flask import Flask
import request
import subprocess

app = Flask(__name__)

@app.route("/")

def ansible_playbook():
    playbook = "docker-node"
    env = request.args.get('env')
    node = request.args.get('node')
    cmd = ["ansible-playbook.sh",env,playbook,node]
    p = subprocess.Popen(cmd, stdout = subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            stdin=subprocess.PIPE)
    out,err = p.communicate()
    return out
if __name__ == "__main__" :
    app.run(host='0.0.0.0')
