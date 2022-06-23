import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("Enter city (chicago, new york city, washington):\n").lower()
    while city not in CITY_DATA.keys():
        print("Invalid city:\n")
        city = input("Enter city (chicago, new york city, washington):\n").lower()
        

    # TO DO: get user input for month (all, january, february, ... , june)
    months = ['january', 'february', 'march', 'april', 'may', 'june' , 'all']
    while True:
        month = input("Enter month (all, january, february, ... , june):\n").lower()
        if month in months:
            break
        else:
            print("Invalid month:\n")
   
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['saterday', 'sunday', 'monday', 'tuesday', 'wendsday', 'thursday' ,'friday', 'all']
    while True:
        day = input("Enter day of week (all, monday, tuesday, ... sunday):\n").lower()
        if day in days:
            break
        else:
            print("Invalid day:\n")
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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['hour'] = df['Start Time'].dt.hour
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month

    popular_month = df['month'].mode()[0]
    print("The most common month: ",popular_month)
    # TO DO: display the most common day of week
    popular_day_of_week = df['day_of_week'].mode()[0]
    print("The most common day of week: ",popular_day_of_week)


    # TO DO: display the most common start hour
    popular_hour = df['hour'].mode()[0]
    print("The most common start hour: ",popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print("The most commonly used start station: ",popular_start_station)
    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print("The most commonly used end station: ",popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['most_frequent'] = df['Start Station'] + '-' + df['End Station']
    most_frequent = df['most_frequent'].mode()[0]
    print("The most frequent combination of start station and end station trip: ",most_frequent)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("The total travel time: ",total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("The mean travel time: ",mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts().to_frame()
    print("The counts of user types: ",user_types)


    # TO DO: Display counts of gender
    try:
        gender = df['Gender'].value_counts().to_frame()
        print("The counts of gender: ",gender)


        # TO DO: Display earliest, most recent, and most common year of birth
        popular_year = df['Birth Year'].mode()[0]
        print("The most common year of birth: ",popular_year)
        most_recent = df['Birth Year'].max()
        print("The most recent: ",most_recent)
        earliest= df['Birth Year'].min()
        print("The most earliest: ",earliest)
    except KeyError:
        print('This data is not available for Washington')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def display_raw_data(df):
    """The fuction takes the name of the city produced by the get_filters fuction as input and returns the raw data of that city as chunks of 5 rows based upon user input.
    """

    print('\nRaw data is available to check... \n')
    i = 0
    while True:
        user_input = input('To View the availbale raw data in chuncks of 5 rows type: Yes \n').lower()
        if user_input not in ['yes', 'no']:
            print('That\'s invalid choice, pleas type yes or no')

        elif user_input == 'yes':
            print(df.iloc[i:i+5])
            i+=5

        elif user_input == 'no':
            print('Thank you')
            break

            
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
