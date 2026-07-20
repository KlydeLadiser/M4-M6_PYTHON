import os


class Project:
    def __init__(self, id_number, title, size, priority):
        self.id_number = int(id_number)
        self.title = title
        self.size = int(size)
        self.priority = int(priority)

    def to_line(self):
        return f"{self.id_number}|{self.title}|{self.size}|{self.priority}\n"

    @staticmethod
    def from_line(line):
        id_number, title, size, priority = line.strip().split("|")
        return Project(id_number, title, size, priority)

    def __str__(self):
        return (
            f"ID: {self.id_number} | Title: {self.title} | "
            f"Size: {self.size} pages | Priority: {self.priority}"
        )


class ProjectManager:
    PROJECTS_FILE = "projects.txt"
    COMPLETED_FILE = "completed.txt"

    def __init__(self):
        self.schedule_queue = []
        self.schedule_created = False
        self._ensure_files_exist()

    def _ensure_files_exist(self):
        for filename in (self.PROJECTS_FILE, self.COMPLETED_FILE):
            if not os.path.exists(filename):
                open(filename, "w").close()

    def input_project(self):
        try:
            id_number = int(input("Enter ID Number: "))
            title = input("Enter Title: ").strip()
            size = int(input("Enter Size (number of pages): "))
            priority = int(
                input("Enter Priority (lower number = more urgent): ")
            )

            if not title:
                raise ValueError("Title cannot be empty.")

            if size <= 0 or priority <= 0:
                raise ValueError("Size and priority must be positive numbers.")

            projects = self._load_all_projects()

            for existing_project in projects:
                if existing_project.id_number == id_number:
                    raise ValueError("A project with that ID already exists.")

            project = Project(id_number, title, size, priority)

            with open(self.PROJECTS_FILE, "a") as file:
                file.write(project.to_line())

            self.schedule_created = False
            self.schedule_queue = []

            print("Project successfully saved.\n")

        except ValueError as error:
            print(f"Invalid input: {error}\n")

        except Exception as error:
            print(f"An unexpected error occurred: {error}\n")

    def _load_all_projects(self):
        projects = []

        try:
            with open(self.PROJECTS_FILE, "r") as file:
                for line in file:
                    if line.strip():
                        projects.append(Project.from_line(line))

        except FileNotFoundError:
            print("Projects file not found.")

        return projects

    def _load_completed_ids(self):
        completed_ids = set()

        try:
            with open(self.COMPLETED_FILE, "r") as file:
                for line in file:
                    if line.strip():
                        completed_ids.add(Project.from_line(line).id_number)
        except FileNotFoundError:
            pass

        return completed_ids

    def _remove_project_from_projects_file(self, completed_project):
        projects = self._load_all_projects()

        with open(self.PROJECTS_FILE, "w") as file:
            for project in projects:
                if project.id_number != completed_project.id_number:
                    file.write(project.to_line())

    def view_all_projects(self):
        projects = self._load_all_projects()

        if not projects:
            print("No projects found.\n")
            return

        print("\n--- All Projects ---")

        for project in projects:
            print(project)

        print()

    def view_one_project(self):
        try:
            search_id = int(input("Enter ID Number to search: "))
            projects = self._load_all_projects()

            for project in projects:
                if project.id_number == search_id:
                    print("\nProject Found:")
                    print(project, "\n")
                    return

            print("No project found with that ID.\n")

        except ValueError:
            print("Invalid ID number entered.\n")

    def view_completed_projects(self):
        try:
            with open(self.COMPLETED_FILE, "r") as file:
                lines = [line for line in file if line.strip()]

            if not lines:
                print("No completed projects yet.\n")
                return

            print("\n--- Completed Projects ---")

            for line in lines:
                print(Project.from_line(line))

            print()

        except FileNotFoundError:
            print("Completed projects file not found.\n")

    def create_schedule(self):
        projects = self._load_all_projects()
        completed_ids = self._load_completed_ids()

        if not projects:
            print("No projects available to schedule.\n")
            return

        filtered_projects = []
        seen_ids = set()

        for project in projects:
            if project.id_number in completed_ids:
                continue

            if project.id_number in seen_ids:
                continue

            seen_ids.add(project.id_number)
            filtered_projects.append(project)

        if not filtered_projects:
            print("No unscheduled projects available.\n")
            self.schedule_queue = []
            self.schedule_created = False
            return

        self.schedule_queue = sorted(
            filtered_projects,
            key=lambda project: (project.priority, project.size)
        )

        self.schedule_created = True

        print("Schedule successfully created.\n")
        self.view_schedule()

    def view_schedule(self):
        if not self.schedule_created:
            print(
                "No schedule has been created yet. "
                "Please create one first.\n"
            )
            return

        if not self.schedule_queue:
            print("The schedule is currently empty.\n")
            return

        print("\n--- Current Schedule (front to rear) ---")

        for project in self.schedule_queue:
            print(project)

        print()

    def get_project(self):
        if not self.schedule_created:
            print(
                "No schedule has been created yet. "
                "Please create one first.\n"
            )
            return

        if not self.schedule_queue:
            print("The queue is empty. No projects left to process.\n")
            return

        completed_project = self.schedule_queue.pop(0)

        try:
            with open(self.COMPLETED_FILE, "a") as file:
                file.write(completed_project.to_line())

            self._remove_project_from_projects_file(completed_project)

            print(f"\nCompleted project: {completed_project}")

        except Exception as error:
            self.schedule_queue.insert(0, completed_project)
            print(f"Error completing project: {error}\n")
            return

        print("\nUpdated Queue:")

        if self.schedule_queue:
            for project in self.schedule_queue:
                print(project)
        else:
            print("(Queue is now empty)")

        print()


def view_projects_menu(manager):
    while True:
        print("--- View Projects ---")
        print("1. One Project")
        print("2. Completed Projects")
        print("3. All Projects")
        print("4. Back to Main Menu")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            manager.view_one_project()

        elif choice == "2":
            manager.view_completed_projects()

        elif choice == "3":
            manager.view_all_projects()

        elif choice == "4":
            break

        else:
            print("Invalid choice. Try again.\n")


def schedule_projects_menu(manager):
    while True:
        print("--- Schedule Projects ---")
        print("1. Create Schedule")
        print("2. View Schedule")
        print("3. Get a Project")
        print("4. Back to Main Menu")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            manager.create_schedule()

        elif choice == "2":
            manager.view_schedule()

        elif choice == "3":
            manager.get_project()

        elif choice == "4":
            break

        else:
            print("Invalid choice. Try again.\n")


def main_menu():
    manager = ProjectManager()

    while True:
        print("========== COPY-TYPING PROJECT SCHEDULER ==========")
        print("1. Input Project Details")
        print("2. View Projects")
        print("3. Schedule Projects")
        print("4. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            manager.input_project()

        elif choice == "2":
            view_projects_menu(manager)

        elif choice == "3":
            schedule_projects_menu(manager)

        elif choice == "4":
            print("Exiting program")
            break

        else:
            print("Invalid choice. Please try again.\n")


if __name__ == "__main__":
    main_menu()