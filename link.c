#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <string.h>
#include <dirent.h>
#include <utime.h>
//author:王浩天
void Mycp(char *fsource,char *ftarget);       //将源目录信息复制到目标目录下
void CopyFile(char *fsource,char *ftarget);  //直接复制
//各种函数原型的应用，参数的设置，查找很多函数资料
int main(int argc,char *argv[])
{
	struct stat statbuf;     //stat结构
	struct utimbuf timeby;  //文件时间结构
	/*
	文件相关三个时间字段stat
	st_atime    最后存取时间
	st_mtime    最后修改时间
	st_ctime    i节点状态的最后更改时间
	struct utimbuf
	{
		time_t actime;         文件数据的最后存取时间
		time_t modtime;        文件数据的最后修改时间
	}
	*/
	DIR * dir;             //DIR结构的指针，指向目录的第一个文件
	if(argc != 3)          //参数出错
	{
		printf("ARGC ERROR!\n");
	}
	else
	{
		/*opendir,closedir
		DIR * opendir(const char *name);
		int closedir(DIR * dir);    关闭指定目录文件，释放相关资源
		*/
		if((dir = opendir(argv[1])) == NULL)
		{
			printf("Source Folder does not exist.\n");    //源文件打开出错
		}
		if((dir = opendir(argv[2])) != NULL)
		{
			printf("File exists!");
			return 0;
		}
		if((dir = opendir(argv[2])) == NULL)
		{
			//时间属性
			/*utime函数:修改文件的存取和修改时间
			int utime(const char *filename,const struct utimbuf buf);
			*/
			//相当于windows中CreateFileD函数功能
			stat(argv[1],&statbuf);
			/*
			stat(const char *file_name,struct stat *buf)
			统计文件名指定的文件属性信息
			*/
			mkdir(argv[2],statbuf.st_mode);    //创建目录
			/*
			mkdir(const char * dir_pathname,mode_t mode)
			rmdir(const char * dir_pathname)  删除
			*/
			timeby.actime = statbuf.st_atime;   //修改时间属性，存取时间
			timeby.modtime = statbuf.st_mtime;  //修改时间
			utime(argv[2],&timeby);//修改文件的存取时间
		}
		
		Mycp(argv[1],argv[2]);    //开始复制
	}
	printf("Copy Finished!\n");
	return 0;
}

void Mycp(char *fsource,char *ftarget)
{
   char source[512];
   char target[512];
   struct stat statbuf;
   struct utimbuf timeby;
   DIR *dir;
   struct dirent * entry;
   /*
   struct dirent
   {ino_t d_ino;                  inode索引节点号
	char d_name[NAME_MAX+1]       文件名
	unsigned char d_type;         文件类型
   }
   */
   strcpy(source,fsource);
   strcpy(target,ftarget);
   dir = opendir(source);     //打开目录,返回指向DIR结构的指针
   while((entry = readdir(dir)) != NULL)  //读目录
   /*
   readdir
   struct dirent *readdir(DIR *dir)
   */
   {
	   if(strcmp(entry->d_name,".") == 0 || strcmp(entry->d_name,"..") == 0)   //判断目录
				continue;
	   if(entry->d_type == 4)//type=4为目录文件
	   {
		   strcat(source,"/");
		   strcat(source,entry->d_name);
		   strcat(target,"/");
		   strcat(target,entry->d_name);
		   //相当于windows中CreateFileD函数功能
		   stat(source,&statbuf);   //统计文件属性信息
		   mkdir(target,statbuf.st_mode);  //创建目标目录
		   timeby.actime = statbuf.st_atime;  
		   timeby.modtime = statbuf.st_mtime;  //修改文件存取和修改时间
		   utime(target,&timeby);
		   Mycp(source,target);
		   strcpy(source,fsource);
		   strcpy(target,ftarget);
	   }
	   if(entry->d_type == 10)//如果是软链接文件
	   {
		   printf("%s\n",entry->d_name);
		   char buf[1024];
		   memset(buf, 0, 1024);
		   ssize_t len=0;
		   strcat(source,"/");
		   strcat(source,entry->d_name);
		   strcat(target,"/");
		   strcat(target,entry->d_name);
		   len = readlink(source, buf, 1024 - 1);
		   buf[len]='\0';
		   printf("%s\n", buf);
		   symlink(buf, target);
		   struct stat statbuff;
		   lstat(source,&statbuf);
		   struct timespec filetime[2] ={statbuf.st_atim,statbuf.st_mtim};
		   utimensat(AT_FDCWD,target,filetime,AT_SYMLINK_NOFOLLOW);
			
		   strcpy(source,fsource);
		   strcpy(target,ftarget);	
			
	   }
	   else     //没有子目录，直接复制
	   {
		   strcat(source,"/");
		   strcat(source,entry->d_name);
		   strcat(target,"/");
		   strcat(target,entry->d_name);
		   CopyFile(source,target);
		   strcpy(source,fsource);
		   strcpy(target,ftarget);
	   }
   }
}

void CopyFile(char *fsource,char *ftarget)
{
	int fd = open(fsource,0);   //打开文件，文件描述符
	int fdr;   //目标文件描述符
	/*
	int open(const char *patename,int_oflg[,mode_t mode])
	若正确，返回文件描述符
	*/
	struct stat statbuf;
	struct utimbuf timeby;
	char BUFFER[1024];    //新开缓冲区，保存数据
	int wordbit;
	stat(fsource,&statbuf);
	fdr = creat(ftarget,statbuf.st_mode);    //创建新文件,返回文件描述符
	/*creat
	int creat(const char *pathname,mode_t mode);
	若正确，返回文件描述符
	*/
	while((wordbit = read(fd,BUFFER,1024)) > 0)   //读取源文件字节数>0
	{
		/*read
		ssize_t read(int fd,void *buf,size_t nbytes);
		正确为0或读写的字节数
		*/
		write(fdr,BUFFER,wordbit);   //写入目标文件
		/*write
		ssize_t write(int fd,void *buf,size_t nbytes);
		*/
	}
	timeby.actime = statbuf.st_atime;  //修改时间属性
	timeby.modtime = statbuf.st_mtime;
	utime(ftarget,&timeby);
	close(fd);  //关闭文件
	close(fdr);
	/*close
	int close(int fd);  文件描述符
	*/
}






