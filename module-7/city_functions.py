#Robert Kiser
#07/12/25
#CSD325
#Module 7.2 Assignment

def country_format(country, city, language='', population=''):

    country = country.capitalize()

    city = city.capitalize()

    if language != '':
        language = f', {language}'

    language = language.title()

    city_country_final = f'{city}, {country}{population}{language}'

    return city_country_final

def main():

    while (True):
        
        country = input('Please enter the name of the country or type "quit" to '\
                        'quit: ')
        
        while (country.isalpha() == False):
            country = input('That input is invalid. Please enter the name of '\
                            'the country or type "quit" to quit: ')

        country = country.lower()

        if country == 'quit':
            break
        
        city = input ('Please enter the name of the city or type "quit" to quit: ')
        while (city.isalpha() == False):
            city = input ('That input is invalid. Please enter the name of the '\
                          'city or type "quit" to quit: ')

        city = city.lower()

        if city == 'quit':
            break

        population = input('Please enter the population, type "quit" to '\
                           'quit, or press enter to skip: ')

        population = population.lower()

        if population == 'quit':
            break

        pop_test = True

        while(pop_test):
            if population == '':
                break
            try:
                population = int(population)
            except:
                population = input('That input is invalid. Please enter the' \
                                   ' population or type "quit" to quit: ')
            else:
                population = f' - population: {population:,}'
                pop_test = False

        language = input('Please enter the official language of the country, type ' \
                         '"quit" to quit, or press enter to skip: ')

        while (language.isalpha() == False):
            if language == '':
                break
            language = input('That input is invalid. Please enter the official ' \
                             'language of the country, type "quit" to quit, or ' \
                             'press enter to skip: ')

        language = language.lower()
    
        if language == 'quit':
            break
                                   
        print(country_format(country, city, language, population))

if __name__ == '__main__':
    main()
