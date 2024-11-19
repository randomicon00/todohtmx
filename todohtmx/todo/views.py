from django.http import HttpResponse
from rest_framework import status
from rest_framework.views import APIView
from .models import Todo, Faq, Statistics


class TodoAPIView(APIView):
    def get(self, _request):
        html = self.render_todo_list()
        return HttpResponse(html)

    def post(self, request):
        task = request.data.get("task")
        if not task or not task.strip():
            return HttpResponse("Please add a task", status=status.HTTP_400_BAD_REQUEST)

        # Create the new task
        Todo.objects.create(task=task)

        # Render the updated list
        html = self.render_container()
        return HttpResponse(html)

    def render_todo_list(self):
        todos = Todo.objects.all()
        tasks = "".join(
            f"<li>{todo.task}  [{todo.get_status_display()}]</li>" for todo in todos
        )
        return f"<ul>{tasks}</ul>"

    def render_container(self):
        fade_out_script = """
        <script>
            window.scrollTo(0, document.body.scrollHeight);
            setTimeout(function () {
                let alertElem = document.getElementById("success-alert");
                if (alertElem) {
                    alertElem.style.transition = "opacity 0.3s ease-out, max-height 0.3s ease-out";
                    alertElem.style.opacity = "0";
                    alertElem.style.maxHeight = "0";
                    setTimeout(function () {
                        alertElem.remove();
                    }, 300);
                }
            }, 1000);
        </script>"""

        return (
            fade_out_script
            + f"""
        <div id="container">
            <div id="add-todo">
                <form
                    hx-post="/todo/api/"
                    hx-swap="outerHTML"
                    hx-target="#container"
                >
                    <input type="text" name="task" placeholder="Task..." />
                    <button type="submit">Add Task</button>
                </form>
            </div>
            <div id="todo-list">
                {self.render_todo_list()}
            </div>
            <div id="success-alert" class="alert">
                Task has been successfully created!
            </div>
        </div>
        """
        )


class FaqAPIView(APIView):
    def get(self, request):
        faqs = Faq.objects.all()
        html = '<div id="faq-container"><ul>'
        for faq in faqs:
            html += f"<li><strong>{faq.question}</strong><p>{faq.answer}</p></li>"
        html += "</ul></div>"
        return HttpResponse(html)


class StatisticsAPIView(APIView):
    def get(self, request):
        html = self.render_statistics()
        return HttpResponse(html)

    def post(self, request):
        stats = self.update_statistics()
        html = self.render_statistics(stats)
        return HttpResponse(html)

    def update_statistics(self):
        stats = Statistics.objects.first()
        if not stats:
            stats = Statistics()
            stats.save()
        else:
            stats.update_stats()
        return stats

    def render_statistics(self, stats=None):
        if stats is None:
            stats = self.update_statistics()
        return f"""
        <div id="statistics-container">
            <p>Pending Count: {stats.pending_count}</p>
            <p>In Progress Count: {stats.in_progress_count}</p>
            <p>Completed Count: {stats.completed_count}</p>
            <p>Archived Count: {stats.archived_count}</p>
        </div>
        """
