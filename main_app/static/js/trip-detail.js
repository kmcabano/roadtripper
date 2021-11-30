const StopToggle = document.getElementById('stop-toggle')

StopToggle.addEventListener('click', showStopForm)

function showStopForm() {
  const target = document.querySelector('.add-stops')
  if (target.style.display !== 'none') {
    target.style.display = 'none'
    StopToggle.innerText = 'Add Stop'
  } else {
    target.style.display = 'block'
    StopToggle.innerText = 'Hide'
  }
}