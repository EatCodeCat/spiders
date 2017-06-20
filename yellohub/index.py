from yellohub.aotuvideo import AotuVideoCrawler
import minspider

if __name__ == '__main__':
    m = minspider.TaskManager([AotuVideoCrawler()])
    m.do_task()
