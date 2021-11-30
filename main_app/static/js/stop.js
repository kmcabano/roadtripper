const arriveInput = document.getElementById('id_arrive')

const arrivePicker = MCDatepicker.create({
  el: '#id_arrive',
  dateFormat: 'yyyy-mm-dd',
  closeOnBlur: true,
  selectedDate: new Date(),
})

arriveInput.addEventListener("click", (evt) => {
  arrivePicker.open()
})

const departInput = document.getElementById('id_depart')

const departPicker = MCDatepicker.create({
  el: '#id_depart',
  dateFormat: 'yyyy-mm-dd',
  closeOnBlur: true,
  selectedDate: new Date(),
})

departInput.addEventListener("click", (evt) => {
  departPicker.open()
})

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