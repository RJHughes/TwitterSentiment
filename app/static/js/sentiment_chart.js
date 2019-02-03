var barData = {
       labels : [
         for (item in labels)
         {
          item
          },
         endfor
 ],
       datasets : [{
         fillColor: "rgba(151,187,205,0.2)",
         strokeColor: "rgba(151,187,205,1)",
         pointColor: "rgba(151,187,205,1)",
         data : [
         for (item in values)
              { item },
             endfor
     ]
         }
       ]
     }
script src="{{ url_for('static', filename='js/sentiment_chart.js') }}" }></script>
var ctx = document.getElementById('myChart').getContext('2d');

steps = 2
max = 3
var chart = new Chart(ctx).Bar(barData, {
       barShowStroke : true,
       scaleShowLabels: true
       }
     );
