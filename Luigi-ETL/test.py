import luigi
from luigi import Task

class HelloWorld(Task):

    def output(self):
        return luigi.LocalTarget('result.txt')

    def run(self):
        print("hello")
        with self.output().open('w') as f:
            f.write('Hello world')

if __name__ == '__main__':
    luigi.run(['HelloWorld', '--local-scheduler'])