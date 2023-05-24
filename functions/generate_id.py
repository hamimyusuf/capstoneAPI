import uuid, shortuuid

def makeId():
    uid = uuid.uuid4()
    s = shortuuid.encode(uid)
    shortid = s[:7]
    return shortid