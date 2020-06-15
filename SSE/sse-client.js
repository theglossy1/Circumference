  var source = new EventSource('/live');
  source.onmessage = function(event) {
    console.log('Incoming date:' + event.data);
  };