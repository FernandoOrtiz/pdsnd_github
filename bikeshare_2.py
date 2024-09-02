import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
available_days =  ['All','Monday', 'Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
available_months = ['All','January', 'February','March','April','May','June','July','August','September','October','November','December']
available_city = CITY_DATA.keys()

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
    while True:
        city = input('What city you wish to analize? (Available options: Chicago, New York City and Washington)\n').lower()

    # TO DO: get user input for month (all, january, february, ... , june)
        month = input('What month filter do you wish to apply? (All, January, February...)\n').lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
        day = input('What day filter do you wish to apply? (All, Monday, Tuesday...)\n').lower()

        if(city in map(str.lower, available_city) and day in map(str.lower, available_days) and month in map(str.lower, available_months)):
            print('-'*40)
            return city, month, day
        else:
            val = input('***Sorry one or more imputs are invalid, try again or type exit to finish.***\n')
            if(val.lower() == 'exit' ):
                exit()


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
    
    df = pd.read_csv(CITY_DATA[city])
    #manipulate data to facilitate filtering date time filtering
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['Year'] = df['Start Time'].dt.year
    df['Month'] = df['Start Time'].dt.month
    df['Day'] = df['Start Time'].dt.day_name
    df['Hour'] = df['Start Time'].dt.hour
    df['Minutes'] = df['Start Time'].dt.minute
    
    if(month != 'all'):
        lower_months = [item.lower() for item in available_months]
        df = df[df['Month'] == lower_months.index(month)]
    if(day != 'all'):
        df = df[df['Day'] == day]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    if('Month' in df.columns):
        print('Most common month is: ',available_months[df['Month'].mode()[0]])

    # TO DO: display the most common day of week
    if('Day' in df.columns):
        print('Most common day is: ',df['Day'].mode()[0])

    # TO DO: display the most common start hour
    if('Hour' in df.columns):
        print('Most common hour is: ',df['Hour'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    if('Start Station' in df.columns):
        print('Most common Start Station is: ',df['Start Station'].mode()[0])

    # TO DO: display most commonly used end station
    if('End Station' in df.columns):
        print('Most common End Station is: ',df['End Station'].mode()[0])

    # TO DO: display most frequent combination of start station and end station trip
    if('End Station' in df.columns and 'Start Station' in df.columns):
        print('Most common Station Combination is: ',(df['Start Station']+' With '+df['End Station']).mode()[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    
    if('Trip Duration' in df.columns):
        # TO DO: display total travel time
        print('The total travel time is: ',df['Trip Duration'].sum())

        # TO DO: display mean travel time
        print('The average travel time is: ',df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    if('User Type' in df.columns):
        print('The count of user types is:\n', df['User Type'].value_counts(),'\n')

    # TO DO: Display counts of gender
    if('Gender' in df.columns):
        print('The count of user genders is:\n', df['Gender'].value_counts(),'\n')


    # TO DO: Display earliest, most recent, and most common year of birth
    if('Birth Year' in df.columns):
        print('The earliest birth year is: ', df['Birth Year'].min())
        print('The most recent birth year is: ', df['Birth Year'].max())
        print('The most common birth year is: ', df['Birth Year'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    """Displays 5 rows of data every time the user prompts for it """
    
    view_data = input('Would you like to display 5 rows of individual data? Yes/No\n').lower()
    loc_start = 0
    while(view_data == 'yes'):
        if(loc_start == 0):
            print(df.iloc[loc_start:loc_start + 5])
        elif((loc_start + 5) <= len(df.index)):
            print(df.iloc[loc_start:loc_start + 5])
        else:
            print(df.iloc[len(df.index) - 5:len(df.index)])
            print('***This is the end of the dataset*** If you wish to continue it will start from the beginning.')
            
        view_data = input('Would you like to continue and display 5 more values? Yes/No\n').lower()
        if(view_data == 'yes' and (loc_start + 5) > len(df.index)):
            loc_start = 0
        elif(view_data == 'yes' and (loc_start + 5) < len(df.index)):
            loc_start = loc_start + 5
            
            

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
