
function startup() {
	swampdragon.open(function() {
    swampdragon.subscribe('notification', 'notification', null, function (context, data) {
      console.log('Successfully subscribed');
    }, function () {
      console.error('Error', arguments);
    });
  });

  swampdragon.onChannelMessage(function(channels, message) {
    if (channels.indexOf('notification') > -1) {
      if (message.action == 'created') {
        createNotification(message.data.text);
      }
    }
  });
}

function createNotification(text, className) {
  new Notification(text);
}