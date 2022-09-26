import argparse

def ParseArgs():
    parser = argparse.ArgumentParser(description='Model Parameters')
    parser.add_argument('--data', default='yelp', type=str, help='name of dataset')
    parser.add_argument('--lr', default=1e-3, type=float, help='learning rate')
    parser.add_argument('--reg', default=1e-6, type=float, help='weight decay regularizer')
    parser.add_argument('--reg_cont', default=1e-8, type=float, help='weight decay regularizer')
    parser.add_argument('--reg_clus', default=0-6, type=float, help='clustering regularizer')
    parser.add_argument('--reg_mean_cont', default=1e-6, type=float, help='clustering regularizer')
    parser.add_argument('--trn_epoch', default=100, type=int, help='number of epochs')
    parser.add_argument('--tst_epoch', default=2, type=int, help='number of epochs')
    parser.add_argument('--trn_batch', default=256, type=int, help='batch size')
    parser.add_argument('--tst_batch', default=256, type=int, help='number of users in a testing batch')
    parser.add_argument('--len_time',  default=801, type=int, help='number of time ')
    return parser.parse_args()
args = ParseArgs()
