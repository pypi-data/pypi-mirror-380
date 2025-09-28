Author: Muhammad Saad
Mail: sd.behance@gmail.com

So this contains stuff that you need to know to use this function.

First of all this is an imputer which uses a machine learning algorithm in order to impute the missing values.So it obviously works a lot better than your traditional .fillna or SimpleImputer. 

We must warn the reader that if a data column has more than 50% of its data missing, you should just remove it ,unless you can figure out any other way to use it. Because it will seriously hamper the performance of whatever model you are training. Regardless its your model, who I am to talk.

MegaImputer:

For importing:

from Magmar import MegaImputer

There are two parameters for this function: "df" and "training_col". In the training_col parameter put the name of the target column of your dataframe (if you intend to keep it inact), otherwise keep it none.

Imputing a typical pandas DataFrame named "df" would look like

df_imputed = MegaImputer(df, training_col = "Target")


Now enjoy :"), I wish to include some more tools in it in the future.

If you find any bugs or want to ask questions drop me a mail.