# geo-pedia
Simpler variant of Wikipedia that only holds structured information about geographical entities.

## Thought process
First thing I wanted to sort out was how the database diagram would look like. For that I have thought of this simple schema:

![Database schema](https://user-images.githubusercontent.com/11338179/131920564-de78ea6d-43e8-40ae-bd92-9281167d8c2b.png)

The schema is holding a simple variant with the tables of *Continent*, *Country* and *City*. We will be creating links between the different tables taking into account the validation logics we are going to hold in the future, so that we can walk through them in an efficient way.

When writing the models in Django's ORM, I have used a base model for the shared fields in all the models, created through inheritance.
