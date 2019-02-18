import tarfile
from os.path import isfile, isdir, join
from urllib.request import urlretrieve

from tqdm import tqdm


def download():
    cifar_folder_path = '../cifar_data'
    cifar_tar_gz = join(cifar_folder_path, 'cifar-10-python.tar.gz')
    cifar_path = join(cifar_folder_path, 'cifar-10-batches-py')

    class DLProgress(tqdm):
        last_block = 0

        def hook(self, block_num=1, block_size=1, total_size=None):
            self.total = total_size
            self.update((block_num - self.last_block) * block_size)
            self.last_block = block_num

    if not isfile(cifar_tar_gz):
        with DLProgress(unit='B', unit_scale=True, miniters=1, desc='CIFAR-10 Dataset') as progress:
            urlretrieve(
                'https://www.cs.toronto.edu/~kriz/cifar-10-python.tar.gz',
                cifar_tar_gz,
                progress.hook)

    if not isdir(cifar_path):
        with tarfile.open('cifar-10-python.tar.gz') as tar:
            tar.extractall()
            tar.close()


if __name__ == '__main__':
    download()
