from django.http import HttpResponse
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Todo, Faq
from .serializers import FaqSerializer


class TodoAPIView(APIView):
    def get(self, _request):

        # Adding tasks to the list
        html = '<div id="container"><ul>'
        todos = Todo.objects.all()
        for todo in todos:
            html += f"<li>{todo.task} - {todo.get_status_display()}</li>"
        html += "</ul></div>"
        return HttpResponse(html)

    def post(self, request):
        task = request.data.get("task")
        Todo.objects.create(task=task)
        if task is None or task.strip() == "":
            return HttpResponse(
                "Please provide a task", status=status.HTTP_400_BAD_REQUEST
            )

        # Adding tasks to the list
        tasks = "<ul>"
        for todo in Todo.objects.all():
            tasks += f"<li>{todo.task} - {todo.get_status_display()}</li>"
        tasks += "</ul>"

        # Adding fade out script
        fadeOutScript = """
        <script>
            window.scrollTo(0, document.body.scrollHeight)
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
            }, 3000);
        </script>"""

        html = (
            fadeOutScript
            + """
        <div id="container">
            <div id="add-todo">
                <form
                    hx-post="http://localhost:8000/todo/api/"
                    hx-swap="outerHTML"
                    hx-target="#container"
                >
                    <input type="text" name="task" placeholder="Task..." />
                    <button type="submit">Add Task</button>
                </form>
            </div>
            <div id="todo-list">"""
            + tasks
            + """</div>
            <div id="success-alert" class="alert">
                Task has been successfully created!
            </div>
        </div>
        """
        )
        return HttpResponse(html)


class FaqAPIView(APIView):
    def get(self, request):
        faqs = Faq.objects.all()
        serializer = FaqSerializer(faqs, many=True)
        return Response(serializer)


# TODO statistics view
class StatisticsView(APIView):
    def get(self, request):
        stats = Statistics.objects.first()
        if not stats:
            stats = Statistics()
            stats.save()
        serializer = StatisticsSerializer(stats)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = StatisticsSerializer(data=stats)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
