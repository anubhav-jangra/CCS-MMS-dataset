import os
import glob
import argparse
import tarfile


### global variables
rename_file = './rename.txt'

def rename_img_files(topic_dir): 
    '''
    Input Arguments:
        topic_dir - file address of a topic containing 'documents', 'images', 'references', 'videos'
    Function renames the images in numerical order using the mapping defined in rename.txt 
    '''

    topic_no = topic_dir.split('topic')[-1]

    with open(rename_file, 'r') as mapping_file:
        mapping = [x.split('\t') for x in mapping_file.read().split('\n')[:-1]]

        for row in mapping:
            if row[0] != 'topic' + str(topic_no):
                continue
            else:
                os.rename(os.path.join(topic_dir, 'images', row[1]), os.path.join(topic_dir, 'images', row[2] + '.jpg'))

def main(args):

    # check if the out_dir exists, if not then create the entire path
    if not os.path.exists('my_folder'):
        os.makedirs('my_folder')
 
    with tarfile.open(args.in_path, 'r:gz') as zip_ref:
        def is_within_directory(directory, target):
            
            abs_directory = os.path.abspath(directory)
            abs_target = os.path.abspath(target)
        
            prefix = os.path.commonprefix([abs_directory, abs_target])
            
            return prefix == abs_directory
        
        def safe_extract(tar, path=".", members=None, *, numeric_owner=False):
        
            for member in tar.getmembers():
                member_path = os.path.join(path, member.name)
                if not is_within_directory(path, member_path):
                    raise Exception("Attempted Path Traversal in Tar File")
        
            tar.extractall(path, members, numeric_owner=numeric_owner) 
            
        
        safe_extract(zip_ref, args.out_path)

    en_dir = os.path.join(args.out_path, 'mms_data', 'en')

    # redo the nomenclature for test part of the dataset. 
    for i in range(1, 21):
        rename_img_files(os.path.join(en_dir, 'test', 'topic' + str(i)))
    
    # redo the nomenclature for dev part of the dataset. 
    for i in range(21, 26):
        rename_img_files(os.path.join(en_dir, 'dev', 'topic' + str(i)))

    

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    
    parser.add_argument('in_path', help="provide address to the mms_data.tar.gz file obtained after following step-1 from README.md") 
    parser.add_argument('out_path', help="provide address to the directory where you want the new dataset to be placed") 
    args = parser.parse_args()

    main(args)
    
