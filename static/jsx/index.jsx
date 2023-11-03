function MainPageContainer() {
    const [showTimePage, setShowTimePage] = React.useState(false);
    const [times, setTimes] = React.useState([]);
    const [day, setDay] = React.useState(null);

    const showAvailableTimes = (times, day) => {
        setTimes(times);
        setDay(day);
        setShowTimePage(true);
    }

    const handleBack = () => {
        setShowTimePage(false);
    }

    return (
        <React.Fragment>
            {showTimePage ? <TimePage setShowTimePage={setShowTimePage} handleBack={handleBack} times={times} day={day}/> : <Scheduler showAvailableTimes={showAvailableTimes} />}
        </React.Fragment>
        )
}


function Scheduler(props) {
    const { showAvailableTimes } = props;

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
        console.log(formInputs)
        fetch('/api/submit_form', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(formInputs),
        })
        .then(response => response.json())
        .then(data => {
            if (data.status == "success") {
                console.log("Success");
                showAvailableTimes(data.times, data.day);
            }
            else {
                console.log(data)
                document.querySelector("#error-message").innerHTML = `<p>${data.message}</p>`;
            }
        })
        .catch(error => console.error('Error sending form', error));
    }

    return (
        <React.Fragment>
            <form>
                <div id="error-message"></div>
                <div className="element">
                    <label htmlFor="day">
                        Enter the date of the reservation you would like
                    </label>
                    <div id="picker">
                        <div id="datepicker" data-date={new Date()} ref={picker}></div>
                        <input type="hidden" id="my_hidden_input" />
                    </div>
                </div> 
                <div className="element">
                    <label htmlFor="start-time">
                        Enter an optional time range and we will only show appointments in that range
                    </label>
                    <input id="start-time" type="time" name="start-time" step="30" required />
                    <input id="end-time" type="time" name="end-time" step="30" required />

                </div>
                <button onClick={submitForm} id="search-time-btn">Search</button>
                
            </form>
        </React.Fragment>
    )
}


function TimePage(props) {

    const { setShowTimePage, times, day, handleBack } = props;

    const handleTimeSelection = (selectedTime) => {
        console.log("Selected time:", selectedTime);

        fetch('/api/book_time', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({"time" : selectedTime, "day": day }),
        })
        .then(response => response.json())
        .then(data => {
            if (data.status == "success") {
                setShowTimePage(false);
            }
        })
        .catch(error => console.error('Error booking a date ', selectedTime, error));

    };

    return (
        <React.Fragment>
            <h1>Pick time</h1>
            <div className="time-blocks">
                {times.map((time, index) => (
                    <button key={index} onClick={() => handleTimeSelection(time)}>
                        {time}
                    </button>
                ))}
            </div>
            <div>
                <button onClick={handleBack}>Back</button>
            </div>
        </React.Fragment>
    )
}