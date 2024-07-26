from io import BytesIO
from PIL import Image,ImageTk
# from playsound import playsound
from py_edamam import PyEdamam
import requests
import tkinter as tk
import webbrowser


WINDOW_TITLE="RECIPE APP"
RECIPE_IMAGE_WIDTH=350
RECIPE_IMAGE_HEIGHT=300


class RecipeApp(object):

    def __init__(self, recipe_app_id, recipe_app_key):
        self.recipe_app_id=recipe_app_id
        self.recipe_app_key= recipe_app_key
        self.window=tk.Tk()

        self.window.geometry("")
        self.window.config(bg="#fcdada")
        self.window.title(WINDOW_TITLE)

        self.search_label = tk.Label(self.window,text="Search Recipe")
        self.search_label.grid(column=0,row=0,padx=5)
        self.search_entry= tk.Entry(master = self.window,width=40)
        self.search_entry.grid(column=1,row=0,padx=5,pady=10)

        self.search_button = tk.Button(self.window,text="Search",highlightbackground="#5c969e",command=self.__run_search_query)
        self.search_button.grid(column=2,row=0,padx=5)




    def __run_search_query(self):
        query = self.search_entry.get()

        recipe = self.__get_recipe(query)

        if recipe:
            recipe_image = recipe.image
            recipe_url =recipe.url

        else:
            recipe_image="https://www.google.com/imgres?q=food%20404&imgurl=https%3A%2F%2Fstatic.vecteezy.com%2Fsystem%2Fresources%2Fthumbnails%2F007%2F415%2F858%2Fsmall%2Fholding-signboard-404-not-found-cute-pear-cartoon-vector.jpg&imgrefurl=https%3A%2F%2Fwww.vecteezy.com%2Ffree-vector%2F404-food&docid=PHMeD3Np7LW8oM&tbnid=buvYbPUOu8T5TM&vet=12ahUKEwj60Mb7ycSHAxUn3jgGHcVwAyMQM3oECFoQAA..i&w=225&h=200&hcb=2&ved=2ahUKEwj60Mb7ycSHAxUn3jgGHcVwAyMQM3oECFoQAA"
            recipe_url=""

        self.__show_image(recipe_image)
        self.__get_ingredients(recipe)




    def __get_recipe(self, query):
        edamam_object =PyEdamam(recipe_appid= self.recipe_app_id,recipe_appkey= self.recipe_app_key)
        query_result = edamam_object.search_recipe(query)

        for recipe in(query_result):
            return recipe
        



    def __show_image(self,image_url):
        response = requests.get(image_url)

        img= Image.open(BytesIO(response.content))
        img=Image.resize(RECIPE_IMAGE_WIDTH, RECIPE_IMAGE_HEIGHT)
        image=ImageTk.PhotoImage(img)
        holder = tk.Label(self.window, image=image)
        holder.photo = image
        holder.grid(column=1,row=6,pady=10)




    def __get_ingredients(self,recipe):
        ingredients = tk.Text(master=self.window,height=15,width=50,bg="#ffa5a5")
        ingredients.grid(column=1,row=4,pady=10)
        ingredients.delete("1.0",tk.END)

        if recipe ==None:
            ingredients.insert(tk.END, "No Recipe fornd for search criteria")
            return 
        
        ingredients.insert(tk.END,"\n"+recipe.label+"\n")
        for ingredients in recipe.ingredient_names:
            ingredients.inset(tk.END,"\n-" + ingredient)




    def run_app(self):
        self.window.mainloop()



if __name__=="__main__":
    APP_ID ="7d30bc38"
    APP_KEY ="c1c5fecdf5b6a724f82a28ad6ecfb5b5"


    recipe_app=RecipeApp(APP_ID,APP_KEY)
    recipe_app.run_app()
