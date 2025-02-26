import os

class TodoList:
    def __init__(self):
        self.tasks = self.load_tasks()

    def load_tasks(self):
        """从文件加载任务"""
        if os.path.exists("tasks.txt"):
            with open("tasks.txt", "r") as f:
                tasks = f.readlines()
            return [task.strip() for task in tasks]
        return []

    def save_tasks(self):
        """将任务保存到文件"""
        with open("tasks.txt", "w") as f:
            for task in self.tasks:
                f.write(task + "\n")

    def add_task(self, task):
        """添加任务"""
        self.tasks.append(task)
        self.save_tasks()

    def delete_task(self, task_index):
        """删除任务"""
        if 0 <= task_index < len(self.tasks):
            self.tasks.pop(task_index)
            self.save_tasks()
        else:
            print("任务编号无效！")

    def show_tasks(self):
        """显示所有任务"""
        if not self.tasks:
            print("没有任务哦！")
        else:
            for idx, task in enumerate(self.tasks, start=1):
                print(f"{idx}. {task}")

def main():
    todo_list = TodoList()

    while True:
        print("\n待办事项应用")
        print("1. 查看任务")
        print("2. 添加任务")
        print("3. 删除任务")
        print("4. 退出")
        
        choice = input("请选择操作（1/2/3/4）：")

        if choice == '1':
            todo_list.show_tasks()
        elif choice == '2':
            task = input("请输入任务内容：")
            todo_list.add_task(task)
        elif choice == '3':
            todo_list.show_tasks()
            try:
                task_index = int(input("请输入任务编号进行删除：")) - 1
                todo_list.delete_task(task_index)
            except ValueError:
                print("请输入有效的编号")
        elif choice == '4':
            print("再见！")
            break
        else:
            print("无效的选项，请重新输入。")

if __name__ == "__main__":
    main()