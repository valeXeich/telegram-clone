export function getCurrentTime() {
    let currentTime = new Date();
    let hours = currentTime.getHours();
    let minutes = currentTime.getMinutes();
    let amOrPm = hours >= 12 ? 'PM' : 'AM';
    hours = hours % 12;
    hours = hours ? hours : 12;
    let formattedTime = hours + ':' + (minutes < 10 ? '0' : '') + minutes + ' ' + amOrPm;
    return formattedTime;
  }