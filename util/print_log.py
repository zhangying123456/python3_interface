import logging

def initLogging(logFilename,e):

  logging.basicConfig(
                    level = logging.INFO,
                    format ='%(asctime)s-%(levelname)s-%(message)s',
                    datefmt = '%y-%m-%d %H:%M',
                    filename = logFilename,
                    filemode = 'a')
  '''
  filename    指定日志文件名
  filemode    指定日志文件打开的模式，w 或 a
  level       指定日志级别，默认 logging.WARNING
  format      指定输出的格式和内容，format 的参考信息如下
  format 输出格式参数
    %(levelno)s:    打印日志级别的数值
    %(levelname)s:  打印日志级别名称
    %(pathname)s:   打印当前执行程序的路径，其实就是sys.argv[0]
    %(filename)s:   打印当前执行程序名
    %(funcName)s:   打印日志的当前函数
    %(lineno)d:     打印日志的当前行号
    %(asctime)s:    打印日志的时间
    %(thread)d:     打印线程ID
    %(threadName)s: 打印线程名称
    %(process)d:    打印进程ID
    %(message)s:    打印日志信息
  datefmt     使用指定的时间格式，format 参数中有 asctime 的话，需要使用 datefmt 指定格式
  '''

  '''
  logging.FileHandler 用于向一个文件输出日志信息
  不过FileHandler会帮你打开这个文件
  它的构造函数是：FileHandler(filename[,mode])filename是文件名，必须指定一个文件名;mode是文件的打开方式
  '''
  fh = logging.FileHandler(logFilename,encoding='utf-8')
  logging.getLogger().addHandler(fh)
  log = logging.exception(e)
  return log
