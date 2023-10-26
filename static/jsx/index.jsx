function IndexPageContainer() {

   const picker = React.useRef(null);
   const [pickedDay, setPickedDay] = React.useState(null);

   React.useEffect(() => {
        const today = new Date();

        if (picker.current) {
            $('#picker').datepicker({
                format: 'YYYY-MM-DD',
                inline: true,
                sideBySide: true,
                todayHighlight: true,
                startDate: today,
            });

            $('#picker').on('changeDate', function(event) {
                const selectedDate = event.date;
                setPickedDay(selectedDate);
              });
        }
   }, []);

   const submitForm = (ev) => {
        ev.preventDefault();

        const formInputs = {
            "day": pickedDay ? pickedDay : new Date(),
            "start": document.querySelector("#start-time").value,
            "end": document.querySelector("#end-time").value,
        }

        fetch('/api/submit_form', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(formInputs),
        })
        .then(response => response.json())
        .then(data => {
            if (data.status == "success") {
                
            }
        })
        .catch(error => console.error('Error sending form', error));
    }

    return (
        <React.Fragment>
            <form>
                <div className="element">
                    <label htmlFor="day">
                        Enter the date of the reservation you would like
                    </label>
                    <div id="picker">
                        <div id="datepicker" data-date={new Date()} ref={picker}></div>
                        <input type="hidden" id="my_hidden_input"></input>
                    </div>
                </div> 
                <div className="element">
                    <label htmlFor="start-time">
                        Enter an optional time range and we will only show appointments in that range
                    </label>
                    <input id="start-time" type="time" name="start-time" step="30" required />
                    <input id="end-time" type="time" name="end-time" step="30" required/>

                </div>
                <button onClick={submitForm} id="search-time-btn">Search</button>
                
            </form>
        </React.Fragment>
    )
}
