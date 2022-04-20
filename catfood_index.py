#! C:\Python39\python.exe
print("content-type: text/html; charset=utf-8\n")
print()
import sys
import codecs
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
print('''<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>fullcalender</title>
    <!-- fullcalender -->
<link href='main.css' rel='stylesheet' />
<script src='main.js'></script>
<script>

      document.addEventListener('DOMContentLoaded', function() {
        var calendarEl = document.getElementById('calendar');
        var calendar = new FullCalendar.Calendar(calendarEl, {
          headerToolbar: {
            left: 'prev,next today',
            center: 'title',
            right: 'dayGridMonth,timeGridWeek,timeGridDay'
          },
          navLinks: true, // can click day/week names to navigate views
          selectable: true,
          selectMirror: true,
          select: function(arg) {
            var title = prompt('일정:');
            if (title) {
              calendar.addEvent({
                title: title,
                start: arg.start,
                end: arg.end,
                allDay: arg.allDay
              })
            }
            calendar.unselect()
          },
          eventClick: function(arg) {
            if (confirm('일정을 지우시겠습니까?')) {
              arg.event.remove()
            }
          },
          editable: true,
          dayMaxEvents: true, // allow "more" link when too many events
          events: [
            ]
        });
        calendar.render();
      });

</script>
  </head>
  <body>
    <div id='calendar'></div>

  </body>
</html>

''')
