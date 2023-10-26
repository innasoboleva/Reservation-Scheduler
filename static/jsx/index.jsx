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
                    <input type="time" name="start-time" step="30" requitred />
                    <input type="time" name="end-time" step="30" required/>

                </div>
              
                <button type="submit" id="search-time-btn">Search</button>
                
            </form>
        </React.Fragment>
    )
}
