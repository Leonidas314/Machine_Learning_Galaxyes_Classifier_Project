from PIL import image

ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg"}

"""chequea extension"""
def allowed_file(filename):
  return "." in filename and filename.rsplit(".",1)[1].lower() in ALLOWED_EXTENSIONS

