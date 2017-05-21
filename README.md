# Yes or No - Game

A "game" where a neural network is trained to classify an object from lots of images.

Very short manual:
1. Download images from google search with `pic_get.py`. Enter the search term.
2. Set path in `pic_sort.py` and execute the script. It will show images from the given path, press `y` or `n` to classify the image. You have to manually move some images (about 1/5 of all) to the validation folders.
3. Use `pic_train.py` to train the neural network. Play around with the parameters in the script to optimize results.
4. As long as there are images in `Pictures/new/`, use `pic_predict.py` to predict those images. They are moved to `Pictures/predicted/`. Correct the predictions with `pic_sort.py` (set correct path first).

I built this in very short time: So, I'm sorry for the handicraft work. It's more just a set of tools.