import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
city_inp=''
month_inp=''
day_inp=''

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    global city_inp
    global month_inp
    global day_inp
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city_inp=input("\nWould you like to see data for:\n\n\t-- Chicago\n\t-- New York City\n\t-- Washington\n\n[Type the city name]\n ").strip().lower()
        if city_inp=="chicago":
            city="chicago"
            break
        elif city_inp=="new york city":
            city="new york city"
            break
        elif city_inp =="washington":
            city="washington"
            break
        else:
            print(f"sorry but the '{city_inp}' is an invalid input try again")

    # get user input for month (all, january, february, ... , june)
    months=['january', 'february', 'march', 'april', 'may', 'june']
    while True:
        month_inp=input("\nWould you like to choose a month to look into or would you like all months\n[Type month name or 'all' ]\n").strip().lower()
        if month_inp in months:
            month=month_inp
            
            break
        elif month_inp=='all':
            month='all'
            
            break
        else:
            print(f"sorry but '{month_inp}' in an invalid input try again")
            

    # get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['monday', 'tuesday', 'wednesday',
            'thursday', 'friday', 'saturday', 'sunday']

    while True:
        day_inp=input("\nWhich day?\nType a day name: [Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or 'all']\n").strip().lower()
        if day_inp in days:
            day=day_inp
            
            break
        elif day_inp=='all':
            day='all'
            
            break
        else:
            print(f"sorry but '{day_inp}' is an invalid input try again")

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    
    df=pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['Month'] = df['Start Time'].dt.month_name()
    df['Day'] = df['Start Time'].dt.day_name()


    if month != 'all':
     
        df = df[df['Month'] == month.title()]
    else:
        pass

  
    if day != 'all':
        
        df = df[df['Day'] == day.title()]


    return df


def time_stats(df):

    print('\nCalculating The Most Frequent Times of Travel...\n')
    # Use 'global' only if absolutely necessary, assuming month_inp and day_inp are defined globally elsewhere
    global month_inp
    global day_inp
    start_time = time.time()

    # display the most common month
    if month_inp == 'all':
        popular_month = df['Month'].mode()[0]
        print(f"Most Popular Start Month: {popular_month}")

    # display the most common day of week (check is only performed if day_inp is 'all')
    if day_inp == 'all':
        popular_day = df['Day'].mode()[0]
        print(f"Most Popular Start day: {popular_day}")

    # display the most common start hour
    # Ensure this is done first as it's an operation that modifies the DataFrame
    df['hour'] = df['Start Time'].dt.hour

    # Calculate mode directly without extra blank line
    popular_hour = df['hour'].mode()[0]
    print(f"Most Popular Start Hour: {popular_hour}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start_station = df['Start Station'].value_counts().index.tolist()[0]
    print(f"Most commonly used start station: {popular_start_station}\n")

    # display most commonly used end station
    popular_end_station = df['End Station'].value_counts().index.tolist()[0]
    print(f"Most commonly used end station: {popular_end_station}\n")

    # display most frequent combination of start station and end station trip
    route_counts = df.groupby(['Start Station', 'End Station']).size()
    route_counts = route_counts.sort_values(ascending=False)
    most_frequent_route = route_counts.head(1)
    print(
        f"Most frequent combination of start station and end station trip: {most_frequent_route}\n")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    SECONDS_PER_MINUTE = 60
    SECONDS_PER_HOUR = 60 * 60
    SECONDS_PER_DAY = 60 * 60 * 24

    # display total travel time
    total_seconds = df['Trip Duration'].sum()
    days = total_seconds // SECONDS_PER_DAY
    total_seconds %= SECONDS_PER_DAY

    hours = total_seconds // SECONDS_PER_HOUR
    total_seconds %= SECONDS_PER_HOUR

    minutes = total_seconds // SECONDS_PER_MINUTE
    total_seconds %= SECONDS_PER_MINUTE

    print(
        f"Total travel time in (d:h:m:s): ({days}:{hours}:{minutes}:{total_seconds})")
    
    # display mean travel time
    seconds_m = df['Trip Duration'].mean()

    days_m = seconds_m / SECONDS_PER_DAY
    seconds_m %= SECONDS_PER_DAY

    hours_m = seconds_m / SECONDS_PER_HOUR
    seconds_m %= SECONDS_PER_HOUR

    minutes_m = seconds_m / SECONDS_PER_MINUTE
    seconds_m = total_seconds % SECONDS_PER_MINUTE

    print(
        f"Average travel time in (d:h:m:s): ({days_m}:{hours_m}:{minutes_m}:{seconds_m})")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_count = df['User Type'].value_counts().to_frame()
    print(f"\nUser types:\n{user_count}\n")
    
    # Display counts of gender
    try:    
        gender_count = df['Gender'].value_counts().to_frame()
        print(f"\nGender:\n{gender_count}\n")
    
    # Display earliest, most recent, and most common year of birth
        earliest_year = df['Birth Year'].min()
        most_recent_year = df['Birth Year'].max()
        most_common_year = df['Birth Year'].mode()[0]
        print(f"\nEarliest birth year : {earliest_year}")
        print(f"\nMost recent birth year: {most_recent_year}")
        print(f"\nMost common birth year: {most_common_year}")
    except KeyError:
        print("\n\nSorry, there's no gender or birth year data for Washington.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def display_raw_data(city):
    """
    The fuction takes the city name from get_filters fuction as input 
    and returns the raw data of that city by chunks of 5 rows.

    Args:
        (str) city - name of the city to return the raw data.
    Returns:
        df - raw data of that city by chunks of 5 rows.
    """

    print('\nRaw data is available to check... \n')

    display_raw = input(
        "View the raw data in chuncks of 5 rows type? [Yes/No]\n> ").strip().lower()

    while display_raw == 'yes':
        try:
            for chunk in pd.read_csv(CITY_DATA[city], index_col=0, chunksize=5):
                print(chunk)
                display_raw = input(
                    "View the raw data in chuncks of 5 rows type? [Yes/No]\n> ").strip().lower()
                if display_raw != 'yes':
                    
                    print('Thank You')
                    break
            break

        except KeyboardInterrupt:
           
            print('Thank you')


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
##check if it is the main file 