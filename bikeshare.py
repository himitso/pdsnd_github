import pandas as pd
import numpy as np
import time

CITY_DATA = { '1': 'chicago.csv',
              '2': 'new_york_city.csv',
              '3': 'washington.csv' }

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
            city=input('Would you like to see data for Chicago enter 1, New York enter 2, or Washington enter 3 ?\n')
            if city not in CITY_DATA:
                print('invalid value please try enter the right city\n')
                continue
            else:
                break
    filtering=input('Would you like to filter the data by month enter number (1) or by day enter number (2)3\n if you do not want to filter at all enter number(3) or if you want filtring by both enter number(4)?\n')
    if filtering=='1':
                day='all' 
 # TO DO: get user input for month (all, january, february, ... , june)
                while True:
                         month=input(' Which month - January, February, March, April, May, or June?\n').lower()
                         if month not in ['all','january','february','march','april','may','june']:
                            print('invalid value please try enter the right month\n ')
                            continue
                         else:
                              break
    elif filtering=='2':
                month='all'                                    
 # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
                while True:
                         day=input( 'Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?\n').lower()
                         if day not in ['all','monday','tuesday','wednesday','thursday','friday','saturday','sunday']:
                            print('invalid value please try enter the right day\n')
                            continue
                         else:
                              break
    elif filtering=='3':
                month='all'
                day='all'
    elif filtering=='4':
                while True:
                         month=input(' Which month - January, February, March, April, May, or June?\n').lower()
                         if month not in ['all','january','february','march','april','may','june']:
                            print('invalid value please try enter the right month\n')
                            continue
                         else:
                              break                                 
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
                while True:
                         day=input( 'Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?\n').lower()
                         if day not in ['all','monday','tuesday','wednesday','thursday','friday','saturday','sunday']:
                            print('invalid value please try enter the right day\n')
                            continue
                         else:
                              break    
        

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
    df = pd.read_csv(CITY_DATA[city])
    
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month, day week and hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january','february','march','april','may','june']
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
    if popular_month==1:
        comon_month='january'
    elif popular_month==2:
        comon_month='february'
    elif popular_month==3:
        comon_month='march'
    elif popular_month==4:
        comon_month='april'
    elif popular_month==5:
        comon_month='may'
    elif popular_month==6:
        comon_month='june'
    print('the most common month: ',comon_month) 



    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print('the most common day of week: ',popular_day) 


    # TO DO: display the most common start hour
    popular_hour = df['hour'].mode()[0]
    print('the most common start hour: ',popular_hour) 


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_st = df['Start Station'].mode()[0]
    print('the most commonly used start station: ',popular_st)
    
    # TO DO: display most commonly used end station
    popular_end = df['End Station'].mode()[0]
    print('the most commonly used end station: ',popular_end)


    # TO DO: display most frequent combination of start station and end station trip
    df['com'] = df['Start Station']+' to '+df['End Station']
    popular_com=df['com'].mode()[0]
    print('the most frequent combination of start station and end station trip: ',popular_com)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel=df['Trip Duration'].sum()
    print('the total travel time: ' ,total_travel,' seconds')
    


    # TO DO: display mean travel time
    mean_travel=df['Trip Duration'].mean()
    print('the mean travel time: ' ,mean_travel,' seconds')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()

    print('the counts of user types:\n',user_types)


    # TO DO: Display counts of gender
    try:
        user_Gender = df['Gender'].value_counts()
        print('the counts of gender:\n',user_Gender)
    # TO DO: Display earliest, most recent, and most common year of birth
        print('\nWhat is the oldest,youngest and most popular year of birth?\n')
        oldest= df['Birth Year'].min()
        print('the oldest: ',oldest)
        youngest = df['Birth Year'].max()
        print('the youngest: ',youngest)
        comon_birth = df['Birth Year'].mode()[0]
        print('the most popular year of birth: ',comon_birth)
       #if user choose washington the message will displayed 
    except:
        print('there is no gender and Birth year data in this city')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)


        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        
        # display raw data upon request by the user 
        start=0
        view_data=input('\n would you like to see raw data?Enter yes or no.\n').lower()
        while True:

            if view_data=='yes':
                print(df.iloc[start:start+5])
                start +=5
                view_data=input('\n would you like to see more raw data?Enter yes or no.\n').lower()
                continue
            else:
                break

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
