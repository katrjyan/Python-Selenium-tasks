from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from validators import url


'''
1. Accepting a URL parameter from the command line
2. Doing some basic validation to avoid the input of invalid values
3. Scanning a web page at a given URL and retrieve the following information:
 3.1. Number of html form elements (with method="get") present in that page 
 3.2. Number of HTML image tags present in that page 
'''

# accepting a URL parameter from the command line 
input_from_command_line= input("PLease, enter the URL of the web page you want to scan: ")
inputed_url=f"https://{input_from_command_line}"


try:
    # activating Chrome browser and maximizing browser window
    driver=webdriver.Chrome()
    driver.maximize_window()

    # checking the validation of the inputed url before opening it
    valid_url=url(inputed_url)

    if valid_url:
        # navigating to the given url
        driver.get(inputed_url)       
        driver.set_page_load_timeout(30)

        # saving the URL validation results in log_info.txt file
        with open("log_info.txt", "a+") as file:
            file.write("The URL is valid." + "\n")
    else:
        with open("log_info.txt", "a+") as file:
            file.write("The URL is invalid." + "\n")
           
    
    try:
        # waiting for form elements to be visible on the UI and locating them
        WebDriverWait(driver, 30).until(EC.visibility_of_elements_located(By.XPATH, "//form[@method='get']"))
        form_elements=driver.find_elements(By.XPATH, "//form[@method='get' or @method='GET']") 
        
        # getting the number of form elements and saving it in log_info.txt file
        number_form_elements=len(form_elements)
        with open("log_info.txt", "a+") as file:
            file.write("The number of html form elements (with method='get') present on the given page is " + str(number_form_elements) + "\n")
  
    except:
        print("Something failed when trying to locate the form elements and count their number!")

     
    try:
        # waiting for image tags to be visible on the UI and locating them
        WebDriverWait(driver, 30).until(EC.visibility_of_elements_located(By.XPATH, "//img[@src]"))
        image_tags=driver.find_elements(By.XPATH, "//img[@src]")
        
        # getting the number of image tags and saving it in log_info.txt file
        number_image_tags=len(image_tags)
        with open("log_info.txt", "a+") as file:
            file.write("The number of html image tags present on the given page is " + str(number_image_tags) + "\n")
    
    except:
        print("Something failed when trying to locate the image tags and count their number!")

# catching the exception
except Exception as e:
    with open("exception.txt", "a+") as file:
        file.write("The following exception raised: " + "\n" + str(e) + "\n")
    
# closing the browser
finally:
    driver.quit() 

print("The task is completed")  