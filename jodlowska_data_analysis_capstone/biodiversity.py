{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Capstone 2: Biodiversity Project"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Introduction\n",
    "You are a biodiversity analyst working for the National Parks Service.  You're going to help them analyze some data about species at various national parks.\n",
    "\n",
    "Note: The data that you'll be working with for this project is *inspired* by real data, but is mostly fictional."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Step 1\n",
    "Import the modules that you'll be using in this assignment:\n",
    "- `from matplotlib import pyplot as plt`\n",
    "- `import pandas as pd`"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "from matplotlib import pyplot as plt\n",
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Step 2\n",
    "You have been given two CSV files. `species_info.csv` with data about different species in our National Parks, including:\n",
    "- The scientific name of each species\n",
    "- The common names of each species\n",
    "- The species conservation status\n",
    "\n",
    "Load the dataset and inspect it:\n",
    "- Load `species_info.csv` into a DataFrame called `species`"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "species = pd.read_csv('species_info.csv')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Inspect each DataFrame using `.head()`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {
    "collapsed": true
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style>\n",
       "    .dataframe thead tr:only-child th {\n",
       "        text-align: right;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: left;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>category</th>\n",
       "      <th>scientific_name</th>\n",
       "      <th>common_names</th>\n",
       "      <th>conservation_status</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Mammal</td>\n",
       "      <td>Clethrionomys gapperi gapperi</td>\n",
       "      <td>Gapper's Red-Backed Vole</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Mammal</td>\n",
       "      <td>Bos bison</td>\n",
       "      <td>American Bison, Bison</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Mammal</td>\n",
       "      <td>Bos taurus</td>\n",
       "      <td>Aurochs, Aurochs, Domestic Cattle (Feral), Dom...</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Mammal</td>\n",
       "      <td>Ovis aries</td>\n",
       "      <td>Domestic Sheep, Mouflon, Red Sheep, Sheep (Feral)</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Mammal</td>\n",
       "      <td>Cervus elaphus</td>\n",
       "      <td>Wapiti Or Elk</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>Mammal</td>\n",
       "      <td>Odocoileus virginianus</td>\n",
       "      <td>White-Tailed Deer</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>Mammal</td>\n",
       "      <td>Sus scrofa</td>\n",
       "      <td>Feral Hog, Wild Pig</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>Mammal</td>\n",
       "      <td>Canis latrans</td>\n",
       "      <td>Coyote</td>\n",
       "      <td>Species of Concern</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>Mammal</td>\n",
       "      <td>Canis lupus</td>\n",
       "      <td>Gray Wolf</td>\n",
       "      <td>Endangered</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>Mammal</td>\n",
       "      <td>Canis rufus</td>\n",
       "      <td>Red Wolf</td>\n",
       "      <td>Endangered</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  category                scientific_name  \\\n",
       "0   Mammal  Clethrionomys gapperi gapperi   \n",
       "1   Mammal                      Bos bison   \n",
       "2   Mammal                     Bos taurus   \n",
       "3   Mammal                     Ovis aries   \n",
       "4   Mammal                 Cervus elaphus   \n",
       "5   Mammal         Odocoileus virginianus   \n",
       "6   Mammal                     Sus scrofa   \n",
       "7   Mammal                  Canis latrans   \n",
       "8   Mammal                    Canis lupus   \n",
       "9   Mammal                    Canis rufus   \n",
       "\n",
       "                                        common_names conservation_status  \n",
       "0                           Gapper's Red-Backed Vole                 NaN  \n",
       "1                              American Bison, Bison                 NaN  \n",
       "2  Aurochs, Aurochs, Domestic Cattle (Feral), Dom...                 NaN  \n",
       "3  Domestic Sheep, Mouflon, Red Sheep, Sheep (Feral)                 NaN  \n",
       "4                                      Wapiti Or Elk                 NaN  \n",
       "5                                  White-Tailed Deer                 NaN  \n",
       "6                                Feral Hog, Wild Pig                 NaN  \n",
       "7                                             Coyote  Species of Concern  \n",
       "8                                          Gray Wolf          Endangered  \n",
       "9                                           Red Wolf          Endangered  "
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "species.head(10)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Step 3\n",
    "Let's start by learning a bit more about our data.  Answer each of the following questions."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "How many different species are in the `species` DataFrame?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {
    "collapsed": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['Clethrionomys gapperi gapperi' 'Bos bison' 'Bos taurus' ...,\n",
      " 'Parthenocissus vitacea' 'Vitis californica' 'Tribulus terrestris']\n"
     ]
    }
   ],
   "source": [
    "print(species.scientific_name.unique())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5541\n"
     ]
    }
   ],
   "source": [
    "print(species.scientific_name.nunique())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['Mammal' 'Bird' 'Reptile' 'Amphibian' 'Fish' 'Vascular Plant'\n",
      " 'Nonvascular Plant']\n"
     ]
    }
   ],
   "source": [
    "print(species.category.unique())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "7\n"
     ]
    }
   ],
   "source": [
    "print(species.category.nunique())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "What are the different values of `category` in `species`?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {
    "collapsed": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['Mammal' 'Bird' 'Reptile' 'Amphibian' 'Fish' 'Vascular Plant'\n",
      " 'Nonvascular Plant']\n"
     ]
    }
   ],
   "source": [
    "print(species.category.unique())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "What are the different values of `conservation_status`?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {
    "collapsed": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[nan 'Species of Concern' 'Endangered' 'Threatened' 'In Recovery']\n"
     ]
    }
   ],
   "source": [
    "print(species.conservation_status.unique())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Step 4\n",
    "Let's start doing some analysis!\n",
    "\n",
    "The column `conservation_status` has several possible values:\n",
    "- `Species of Concern`: declining or appear to be in need of conservation\n",
    "- `Threatened`: vulnerable to endangerment in the near future\n",
    "- `Endangered`: seriously at risk of extinction\n",
    "- `In Recovery`: formerly `Endangered`, but currnetly neither in danger of extinction throughout all or a significant portion of its range\n",
    "\n",
    "We'd like to count up how many species meet each of these criteria.  Use `groupby` to count how many `scientific_name` meet each of these criteria."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "status_count = species.groupby('conservation_status').scientific_name.count().reset_index()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  conservation_status  scientific_name\n",
      "0          Endangered               16\n",
      "1         In Recovery                4\n",
      "2  Species of Concern              161\n",
      "3          Threatened               10\n"
     ]
    }
   ],
   "source": [
    "print(status_count)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "As we saw before, there are far more than 200 species in the `species` table.  Clearly, only a small number of them are categorized as needing some sort of protection.  The rest have `conservation_status` equal to `None`.  Because `groupby` does not include `None`, we will need to fill in the null values.  We can do this using `.fillna`.  We pass in however we want to fill in our `None` values as an argument.\n",
    "\n",
    "Paste the following code and run it to see replace `None` with `No Intervention`:\n",
    "```python\n",
    "species.fillna('No Intervention', inplace=True)\n",
    "```"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "species.fillna('No Intervention', inplace=True)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Great! Now run the same `groupby` as before to see how many species require `No Protection`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {
    "collapsed": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  conservation_status  scientific_name\n",
      "0          Endangered               16\n",
      "1         In Recovery                4\n",
      "2     No Intervention             5633\n",
      "3  Species of Concern              161\n",
      "4          Threatened               10\n"
     ]
    }
   ],
   "source": [
    "status_count = species.groupby('conservation_status').scientific_name.count().reset_index()\n",
    "print(status_count)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Let's use `plt.bar` to create a bar chart.  First, let's sort the columns by how many species are in each categories.  We can do this using `.sort_values`.  We use the the keyword `by` to indicate which column we want to sort by.\n",
    "\n",
    "Paste the following code and run it to create a new DataFrame called `protection_counts`, which is sorted by `scientific_name`:\n",
    "```python\n",
    "protection_counts = species.groupby('conservation_status')\\\n",
    "    .scientific_name.count().reset_index()\\\n",
    "    .sort_values(by='scientific_name')\n",
    "```"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {
    "collapsed": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  conservation_status  scientific_name\n",
      "1         In Recovery                4\n",
      "4          Threatened               10\n",
      "0          Endangered               16\n",
      "3  Species of Concern              161\n",
      "2     No Intervention             5633\n"
     ]
    }
   ],
   "source": [
    "protection_counts = species.groupby('conservation_status')\\\n",
    "    .scientific_name.count().reset_index()\\\n",
    "    .sort_values(by='scientific_name')\n",
    "print(protection_counts)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Now let's create a bar chart!\n",
    "1. Start by creating a wide figure with `figsize=(10, 4)`\n",
    "1. Start by creating an axes object called `ax` using `plt.subplot`.\n",
    "2. Create a bar chart whose heights are equal to `scientific_name` column of `protection_counts`.\n",
    "3. Create an x-tick for each of the bars.\n",
    "4. Label each x-tick with the label from `conservation_status` in `protection_counts`\n",
    "5. Label the y-axis `Number of Species`\n",
    "6. Title the graph `Conservation Status by Species`\n",
    "7. Plot the grap using `plt.show()`"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 139,
   "metadata": {
    "collapsed": true
   },
   "outputs": [
    {
     "data": {
      "image/png": "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\ncZMkSeoJEzdJkqSeMHGTJEnqCRM3SZKknjBxkyRJ6gkTN0mSpJ4wcZMkSeoJEzdJkqSeGGniluS6\nJJcmuTjJsla3VZKlSa5q11sOLH90kquTXJlkn4H63Vs/Vyc5IUlGGbckSdJcNBMjbs+pqt2qanG7\nfRRwdlXtDJzdbpNkF+Bg4EnAvsCJSea1Nh8ADgN2bpd9ZyBuSZKkOWU2dpXuD5zSyqcABwzUn1pV\n91TVtcDVwB5JtgE2q6rzqqqAjw60kSRJWmeMOnEr4D+TXJDk8Fa3sKpuauWbgYWtvC1ww0DbG1vd\ntq08vn4VSQ5PsizJspUrV07XY5AkSZoT1h9x/3tX1YokjwaWJrli8M6qqiQ1XSurqpOAkwAWL148\nbf1KkiTNBSMdcauqFe36VuBzwB7ALW33J+361rb4CmD7gebbtboVrTy+XpIkaZ0yssQtycZJNh0r\nAy8ALgNOAw5pix0CfKGVTwMOTrJRkp3oDkI4v+1WvT3Jnu1o0lcPtJEkSVpnjHJX6ULgc+3MHesD\nn6iq/0jyLWBJktcB1wMHAlTV8iRLgMuBe4Ejquq+1tcbgZOB+cCX2kWSJGmdMrLEraquAX51gvrv\nA8+bpM2xwLET1C8Ddp3uGCVJkvrEf06QJEnqCRM3SZKknjBxkyRJ6gkTN0mSpJ4wcZMkSeoJEzdJ\nkqSeMHGTJEnqCRM3SZKknjBxkyRJ6gkTN0mSpJ4wcZMkSeoJEzdJkqSeMHGTJEnqCRM3SZKknjBx\nkyRJ6gkTN0mSpJ4wcZMkSeoJEzdJkqSeMHGTJEnqCRM3SZKknjBxkyRJ6gkTN0mSpJ4wcZMkSeoJ\nEzdJkqSeWG3iluRlSTZt5WOS/FuSp4w+NEmSJA0aZsTtL6vqjiR7A88HPgx8YLRhSZIkabxhErf7\n2vV+wElVdQaw4ehCkiRJ0kSGSdxWJPkgcBDwxSQbDdlOkiRJ02iYBOxA4Exgn6r6IbAV8CfDriDJ\nvCQXJTm93d4qydIkV7XrLQeWPTrJ1UmuTLLPQP3uSS5t952QJEM/QkmSpLXEahO3qvoxcCuwd6u6\nF7hqDdZxJPCdgdtHAWdX1c7A2e02SXYBDgaeBOwLnJhkXmvzAeAwYOd22XcN1i9JkrRWGOao0rcB\nfwYc3ao2AD42TOdJtqObG/ehger9gVNa+RTggIH6U6vqnqq6Frga2CPJNsBmVXVeVRXw0YE2kiRJ\n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\nJm6SJEk9YeImSZLUEyZukiRJPWHiJkmS1BMmbpIkST1h4iZJktQTJm6SJEk9YeImSZLUEyZukiRJ\nPWHiJkmS1BMmbpIkST1h4iZJktQTJm6SJEk9MbLELclHktya5LKBuq2SLE1yVbvecuC+o5NcneTK\nJPsM1O+e5NJ23wlJMqqYJUmS5rJRjridDOw7ru4o4Oyq2hk4u90myS7AwcCTWpsTk8xrbT4AHAbs\n3C7j+5QkSVonjCxxq6qvAreNq94fOKWVTwEOGKg/taruqaprgauBPZJsA2xWVedVVQEfHWgjSZK0\nTpnpOW4Lq+qmVr4ZWNjK2wI3DCx3Y6vbtpXH108oyeFJliVZtnLlyumLWpIkaQ6YtYMT2ghaTXOf\nJ1XV4qpavGDBgunsWpIkadbNdOJ2S9v9Sbu+tdWvALYfWG67VreilcfXS5IkrXNmOnE7DTiklQ8B\nvjBQf3CSjZLsRHcQwvltt+rtSfZsR5O+eqCNJEnSOmX9UXWc5JPAs4Gtk9wIvA04DliS5HXA9cCB\nAFW1PMkS4HLgXuCIqrqvdfVGuiNU5wNfahdJkqR1zsgSt6p6+SR3PW+S5Y8Fjp2gfhmw6zSGJkmS\n1Ev+c4IkSVJPmLhJkiT1hImbJElST5i4SZIk9YSJmyRJUk+YuEmSJPWEiZskSVJPmLhJkiT1hImb\nJElST5i4SZIk9YSJmyRJUk+YuEmSJPWEiZskSVJPmLhJkiT1hImbJElST5i4SZIk9YSJmyRJUk+Y\nuEmSJPWEiZskSVJPmLhJkiT1hImbJElST5i4SZIk9YSJmyRJUk+YuEmSJPWEiZskSVJPrD/bAUiS\n+mHRUWfMdghrneuO22+2Q1DPOOImSZLUEyZukiRJPdGbxC3JvkmuTHJ1kqNmOx5JkqSZ1ovELck8\n4J+A3wB2AV6eZJfZjUqSJGlm9eXghD2Aq6vqGoAkpwL7A5fPalTqBSdUT69RTKZ2G00/J71La6dU\n1WzHsFpJXgrsW1W/226/CnhaVf3+uOUOBw5vN38RuHJGA527tga+N9tBaLXcTv3gdpr73Eb94HZ6\nsB2rasHqFurLiNtQquok4KTZjmOuSbKsqhbPdhyamtupH9xOc5/bqB/cTg9NL+a4ASuA7Qdub9fq\nJEmS1hl9Sdy+BeycZKckGwIHA6fNckySJEkzqhe7Sqvq3iS/D5wJzAM+UlXLZzmsPnH3cT+4nfrB\n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\nFaOIAAAAAElFTkSuQmCC\n",
      "text/plain": [
       "<matplotlib.figure.Figure at 0x11e8af128>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.figure(figsize=(10,4))\n",
    "plt.bar(range(len(protection_counts.scientific_name)), protection_counts.scientific_name)\n",
    "ax = plt.subplot()\n",
    "ax.set_xticks(range(len(protection_counts.scientific_name)))\n",
    "ax.set_xticklabels(protection_counts.conservation_status)\n",
    "ax.set_ylabel('Number of Species')\n",
    "ax.set_title('Status of Species')\n",
    "plt.savefig('status_species.png')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Step 4\n",
    "Are certain types of species more likely to be endangered?"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Let's create a new column in `species` called `is_protected`, which is `True` if `conservation_status` is not equal to `No Intervention`, and `False` otherwise."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "species['is_protected'] = species.conservation_status.apply(lambda x: False if x == 'No Intervention' else True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style>\n",
       "    .dataframe thead tr:only-child th {\n",
       "        text-align: right;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: left;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>category</th>\n",
       "      <th>scientific_name</th>\n",
       "      <th>common_names</th>\n",
       "      <th>conservation_status</th>\n",
       "      <th>is_protected</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Mammal</td>\n",
       "      <td>Clethrionomys gapperi gapperi</td>\n",
       "      <td>Gapper's Red-Backed Vole</td>\n",
       "      <td>No Intervention</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Mammal</td>\n",
       "      <td>Bos bison</td>\n",
       "      <td>American Bison, Bison</td>\n",
       "      <td>No Intervention</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Mammal</td>\n",
       "      <td>Bos taurus</td>\n",
       "      <td>Aurochs, Aurochs, Domestic Cattle (Feral), Dom...</td>\n",
       "      <td>No Intervention</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Mammal</td>\n",
       "      <td>Ovis aries</td>\n",
       "      <td>Domestic Sheep, Mouflon, Red Sheep, Sheep (Feral)</td>\n",
       "      <td>No Intervention</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Mammal</td>\n",
       "      <td>Cervus elaphus</td>\n",
       "      <td>Wapiti Or Elk</td>\n",
       "      <td>No Intervention</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>Mammal</td>\n",
       "      <td>Odocoileus virginianus</td>\n",
       "      <td>White-Tailed Deer</td>\n",
       "      <td>No Intervention</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>Mammal</td>\n",
       "      <td>Sus scrofa</td>\n",
       "      <td>Feral Hog, Wild Pig</td>\n",
       "      <td>No Intervention</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>Mammal</td>\n",
       "      <td>Canis latrans</td>\n",
       "      <td>Coyote</td>\n",
       "      <td>Species of Concern</td>\n",
       "      <td>True</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>Mammal</td>\n",
       "      <td>Canis lupus</td>\n",
       "      <td>Gray Wolf</td>\n",
       "      <td>Endangered</td>\n",
       "      <td>True</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>Mammal</td>\n",
       "      <td>Canis rufus</td>\n",
       "      <td>Red Wolf</td>\n",
       "      <td>Endangered</td>\n",
       "      <td>True</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  category                scientific_name  \\\n",
       "0   Mammal  Clethrionomys gapperi gapperi   \n",
       "1   Mammal                      Bos bison   \n",
       "2   Mammal                     Bos taurus   \n",
       "3   Mammal                     Ovis aries   \n",
       "4   Mammal                 Cervus elaphus   \n",
       "5   Mammal         Odocoileus virginianus   \n",
       "6   Mammal                     Sus scrofa   \n",
       "7   Mammal                  Canis latrans   \n",
       "8   Mammal                    Canis lupus   \n",
       "9   Mammal                    Canis rufus   \n",
       "\n",
       "                                        common_names conservation_status  \\\n",
       "0                           Gapper's Red-Backed Vole     No Intervention   \n",
       "1                              American Bison, Bison     No Intervention   \n",
       "2  Aurochs, Aurochs, Domestic Cattle (Feral), Dom...     No Intervention   \n",
       "3  Domestic Sheep, Mouflon, Red Sheep, Sheep (Feral)     No Intervention   \n",
       "4                                      Wapiti Or Elk     No Intervention   \n",
       "5                                  White-Tailed Deer     No Intervention   \n",
       "6                                Feral Hog, Wild Pig     No Intervention   \n",
       "7                                             Coyote  Species of Concern   \n",
       "8                                          Gray Wolf          Endangered   \n",
       "9                                           Red Wolf          Endangered   \n",
       "\n",
       "   is_protected  \n",
       "0         False  \n",
       "1         False  \n",
       "2         False  \n",
       "3         False  \n",
       "4         False  \n",
       "5         False  \n",
       "6         False  \n",
       "7          True  \n",
       "8          True  \n",
       "9          True  "
      ]
     },
     "execution_count": 36,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "species.head(10)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Let's group by *both* `category` and `is_protected`.  Save your results to `category_counts`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "category_counts = species.groupby(['category', 'is_protected'])['scientific_name'].count().reset_index()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Examine `category_count` using `head()`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "metadata": {
    "collapsed": true
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style>\n",
       "    .dataframe thead tr:only-child th {\n",
       "        text-align: right;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: left;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>category</th>\n",
       "      <th>is_protected</th>\n",
       "      <th>scientific_name</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Amphibian</td>\n",
       "      <td>False</td>\n",
       "      <td>73</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Amphibian</td>\n",
       "      <td>True</td>\n",
       "      <td>7</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Bird</td>\n",
       "      <td>False</td>\n",
       "      <td>442</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Bird</td>\n",
       "      <td>True</td>\n",
       "      <td>79</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Fish</td>\n",
       "      <td>False</td>\n",
       "      <td>116</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>Fish</td>\n",
       "      <td>True</td>\n",
       "      <td>11</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>Mammal</td>\n",
       "      <td>False</td>\n",
       "      <td>176</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>Mammal</td>\n",
       "      <td>True</td>\n",
       "      <td>38</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>Nonvascular Plant</td>\n",
       "      <td>False</td>\n",
       "      <td>328</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>Nonvascular Plant</td>\n",
       "      <td>True</td>\n",
       "      <td>5</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "            category  is_protected  scientific_name\n",
       "0          Amphibian         False               73\n",
       "1          Amphibian          True                7\n",
       "2               Bird         False              442\n",
       "3               Bird          True               79\n",
       "4               Fish         False              116\n",
       "5               Fish          True               11\n",
       "6             Mammal         False              176\n",
       "7             Mammal          True               38\n",
       "8  Nonvascular Plant         False              328\n",
       "9  Nonvascular Plant          True                5"
      ]
     },
     "execution_count": 57,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "category_counts.head(10)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "It's going to be easier to view this data if we pivot it.  Using `pivot`, rearange `category_counts` so that:\n",
    "- `columns` is `conservation_status`\n",
    "- `index` is `category`\n",
    "- `values` is `scientific_name`\n",
    "\n",
    "Save your pivoted data to `category_pivot`. Remember to `reset_index()` at the end."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "category_pivot = category_counts.pivot(columns='is_protected',\n",
    "                                      index='category',\n",
    "                                      values='scientific_name')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Examine `category_pivot`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "metadata": {
    "collapsed": true
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style>\n",
       "    .dataframe thead tr:only-child th {\n",
       "        text-align: right;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: left;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th>is_protected</th>\n",
       "      <th>False</th>\n",
       "      <th>True</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>category</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>Amphibian</th>\n",
       "      <td>73</td>\n",
       "      <td>7</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Bird</th>\n",
       "      <td>442</td>\n",
       "      <td>79</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Fish</th>\n",
       "      <td>116</td>\n",
       "      <td>11</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Mammal</th>\n",
       "      <td>176</td>\n",
       "      <td>38</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Nonvascular Plant</th>\n",
       "      <td>328</td>\n",
       "      <td>5</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Reptile</th>\n",
       "      <td>74</td>\n",
       "      <td>5</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Vascular Plant</th>\n",
       "      <td>4424</td>\n",
       "      <td>46</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "is_protected       False  True \n",
       "category                       \n",
       "Amphibian             73      7\n",
       "Bird                 442     79\n",
       "Fish                 116     11\n",
       "Mammal               176     38\n",
       "Nonvascular Plant    328      5\n",
       "Reptile               74      5\n",
       "Vascular Plant      4424     46"
      ]
     },
     "execution_count": 59,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "category_pivot.head(10)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Use the `.columns` property to  rename the categories `True` and `False` to something more description:\n",
    "- Leave `category` as `category`\n",
    "- Rename `False` to `not_protected`\n",
    "- Rename `True` to `protected`"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "metadata": {
    "collapsed": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "is_protected       False  True \n",
      "category                       \n",
      "Amphibian             73      7\n",
      "Bird                 442     79\n",
      "Fish                 116     11\n",
      "Mammal               176     38\n",
      "Nonvascular Plant    328      5\n",
      "Reptile               74      5\n",
      "Vascular Plant      4424     46\n"
     ]
    }
   ],
   "source": [
    "print(category_pivot)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "metadata": {},
   "outputs": [],
   "source": [
    "category_pivot.columns = ['not_protected','protected']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "                   not_protected  protected\n",
      "category                                   \n",
      "Amphibian                     73          7\n",
      "Bird                         442         79\n",
      "Fish                         116         11\n",
      "Mammal                       176         38\n",
      "Nonvascular Plant            328          5\n",
      "Reptile                       74          5\n",
      "Vascular Plant              4424         46\n"
     ]
    }
   ],
   "source": [
    "print(category_pivot)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Let's create a new column of `category_pivot` called `percent_protected`, which is equal to `protected` (the number of species that are protected) divided by `protected` plus `not_protected` (the total number of species)."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 72,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "category_pivot['percent_protected'] = category_pivot.apply(lambda row:\n",
    "                                                           row['protected'] / (row['protected'] + row['not_protected']),\n",
    "                                                          axis=1\n",
    "                                                          )"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Examine `category_pivot`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 74,
   "metadata": {
    "collapsed": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "                   not_protected  protected  percent_protected\n",
      "category                                                      \n",
      "Amphibian                     73          7           0.087500\n",
      "Bird                         442         79           0.151631\n",
      "Fish                         116         11           0.086614\n",
      "Mammal                       176         38           0.177570\n",
      "Nonvascular Plant            328          5           0.015015\n",
      "Reptile                       74          5           0.063291\n",
      "Vascular Plant              4424         46           0.010291\n"
     ]
    }
   ],
   "source": [
    "print(category_pivot)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "It looks like species in category `Mammal` are more likely to be endangered than species in `Bird`.  We're going to do a significance test to see if this statement is true.  Before you do the significance test, consider the following questions:\n",
    "- Is the data numerical or categorical?\n",
    "- How many pieces of data are you comparing?"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Based on those answers, you should choose to do a *chi squared test*.  In order to run a chi squared test, we'll need to create a contingency table.  Our contingency table should look like this:\n",
    "\n",
    "||protected|not protected|\n",
    "|-|-|-|\n",
    "|Mammal|?|?|\n",
    "|Bird|?|?|\n",
    "\n",
    "Create a table called `contingency` and fill it in with the correct numbers"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 81,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "contingency = [[79, 442],\n",
    "               [38, 176]]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "In order to perform our chi square test, we'll need to import the correct function from scipy.  Past the following code and run it:\n",
    "```py\n",
    "from scipy.stats import chi2_contingency\n",
    "```"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 75,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "from scipy.stats import chi2_contingency"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Now run `chi2_contingency` with `contingency`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 82,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "chi2, pval, dof, expected = chi2_contingency(contingency)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 83,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0.445901703047\n"
     ]
    }
   ],
   "source": [
    "print(pval)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "It looks like this difference isn't significant!\n",
    "\n",
    "Let's test another.  Is the difference between `Reptile` and `Mammal` significant?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 84,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "contingency2 = [[5, 74],\n",
    "               [38, 176]]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 85,
   "metadata": {},
   "outputs": [],
   "source": [
    "chi2, pval, dof, expected = chi2_contingency(contingency2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 86,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0.0233846521487\n"
     ]
    }
   ],
   "source": [
    "print(pval)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Yes! It looks like there is a significant difference between `Reptile` and `Mammal`!"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Step 5"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Conservationists have been recording sightings of different species at several national parks for the past 7 days.  They've saved sent you their observations in a file called `observations.csv`.  Load `observations.csv` into a variable called `observations`, then use `head` to view the data."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 96,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "observations = pd.read_csv('observations.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 97,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style>\n",
       "    .dataframe thead tr:only-child th {\n",
       "        text-align: right;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: left;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>scientific_name</th>\n",
       "      <th>park_name</th>\n",
       "      <th>observations</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Vicia benghalensis</td>\n",
       "      <td>Great Smoky Mountains National Park</td>\n",
       "      <td>68</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Neovison vison</td>\n",
       "      <td>Great Smoky Mountains National Park</td>\n",
       "      <td>77</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Prunus subcordata</td>\n",
       "      <td>Yosemite National Park</td>\n",
       "      <td>138</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Abutilon theophrasti</td>\n",
       "      <td>Bryce National Park</td>\n",
       "      <td>84</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Githopsis specularioides</td>\n",
       "      <td>Great Smoky Mountains National Park</td>\n",
       "      <td>85</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>Elymus virginicus var. virginicus</td>\n",
       "      <td>Yosemite National Park</td>\n",
       "      <td>112</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>Spizella pusilla</td>\n",
       "      <td>Yellowstone National Park</td>\n",
       "      <td>228</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>Elymus multisetus</td>\n",
       "      <td>Great Smoky Mountains National Park</td>\n",
       "      <td>39</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>Lysimachia quadrifolia</td>\n",
       "      <td>Yosemite National Park</td>\n",
       "      <td>168</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>Diphyscium cumberlandianum</td>\n",
       "      <td>Yellowstone National Park</td>\n",
       "      <td>250</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                     scientific_name                            park_name  \\\n",
       "0                 Vicia benghalensis  Great Smoky Mountains National Park   \n",
       "1                     Neovison vison  Great Smoky Mountains National Park   \n",
       "2                  Prunus subcordata               Yosemite National Park   \n",
       "3               Abutilon theophrasti                  Bryce National Park   \n",
       "4           Githopsis specularioides  Great Smoky Mountains National Park   \n",
       "5  Elymus virginicus var. virginicus               Yosemite National Park   \n",
       "6                   Spizella pusilla            Yellowstone National Park   \n",
       "7                  Elymus multisetus  Great Smoky Mountains National Park   \n",
       "8             Lysimachia quadrifolia               Yosemite National Park   \n",
       "9         Diphyscium cumberlandianum            Yellowstone National Park   \n",
       "\n",
       "   observations  \n",
       "0            68  \n",
       "1            77  \n",
       "2           138  \n",
       "3            84  \n",
       "4            85  \n",
       "5           112  \n",
       "6           228  \n",
       "7            39  \n",
       "8           168  \n",
       "9           250  "
      ]
     },
     "execution_count": 97,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "observations.head(10)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Some scientists are studying the number of sheep sightings at different national parks.  There are several different scientific names for different types of sheep.  We'd like to know which rows of `species` are referring to sheep.  Notice that the following code will tell us whether or not a word occurs in a string:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 1,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Does \"Sheep\" occur in this string?\n",
    "str1 = 'This string contains Sheep'\n",
    "'Sheep' in str1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Does \"Sheep\" occur in this string?\n",
    "str2 = 'This string contains Cows'\n",
    "'Sheep' in str2"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Use `apply` and a `lambda` function to create a new column in `species` called `is_sheep` which is `True` if the `common_names` contains `'Sheep'`, and `False` otherwise."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 99,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "species['is_sheep'] = species.common_names.apply(\n",
    "    lambda x: True if 'Sheep' in x\n",
    "    else False\n",
    ")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 100,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style>\n",
       "    .dataframe thead tr:only-child th {\n",
       "        text-align: right;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: left;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>category</th>\n",
       "      <th>scientific_name</th>\n",
       "      <th>common_names</th>\n",
       "      <th>conservation_status</th>\n",
       "      <th>is_protected</th>\n",
       "      <th>is_sheep</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Mammal</td>\n",
       "      <td>Clethrionomys gapperi gapperi</td>\n",
       "      <td>Gapper's Red-Backed Vole</td>\n",
       "      <td>No Intervention</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Mammal</td>\n",
       "      <td>Bos bison</td>\n",
       "      <td>American Bison, Bison</td>\n",
       "      <td>No Intervention</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Mammal</td>\n",
       "      <td>Bos taurus</td>\n",
       "      <td>Aurochs, Aurochs, Domestic Cattle (Feral), Dom...</td>\n",
       "      <td>No Intervention</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Mammal</td>\n",
       "      <td>Ovis aries</td>\n",
       "      <td>Domestic Sheep, Mouflon, Red Sheep, Sheep (Feral)</td>\n",
       "      <td>No Intervention</td>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Mammal</td>\n",
       "      <td>Cervus elaphus</td>\n",
       "      <td>Wapiti Or Elk</td>\n",
       "      <td>No Intervention</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>Mammal</td>\n",
       "      <td>Odocoileus virginianus</td>\n",
       "      <td>White-Tailed Deer</td>\n",
       "      <td>No Intervention</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>Mammal</td>\n",
       "      <td>Sus scrofa</td>\n",
       "      <td>Feral Hog, Wild Pig</td>\n",
       "      <td>No Intervention</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>Mammal</td>\n",
       "      <td>Canis latrans</td>\n",
       "      <td>Coyote</td>\n",
       "      <td>Species of Concern</td>\n",
       "      <td>True</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>Mammal</td>\n",
       "      <td>Canis lupus</td>\n",
       "      <td>Gray Wolf</td>\n",
       "      <td>Endangered</td>\n",
       "      <td>True</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>Mammal</td>\n",
       "      <td>Canis rufus</td>\n",
       "      <td>Red Wolf</td>\n",
       "      <td>Endangered</td>\n",
       "      <td>True</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  category                scientific_name  \\\n",
       "0   Mammal  Clethrionomys gapperi gapperi   \n",
       "1   Mammal                      Bos bison   \n",
       "2   Mammal                     Bos taurus   \n",
       "3   Mammal                     Ovis aries   \n",
       "4   Mammal                 Cervus elaphus   \n",
       "5   Mammal         Odocoileus virginianus   \n",
       "6   Mammal                     Sus scrofa   \n",
       "7   Mammal                  Canis latrans   \n",
       "8   Mammal                    Canis lupus   \n",
       "9   Mammal                    Canis rufus   \n",
       "\n",
       "                                        common_names conservation_status  \\\n",
       "0                           Gapper's Red-Backed Vole     No Intervention   \n",
       "1                              American Bison, Bison     No Intervention   \n",
       "2  Aurochs, Aurochs, Domestic Cattle (Feral), Dom...     No Intervention   \n",
       "3  Domestic Sheep, Mouflon, Red Sheep, Sheep (Feral)     No Intervention   \n",
       "4                                      Wapiti Or Elk     No Intervention   \n",
       "5                                  White-Tailed Deer     No Intervention   \n",
       "6                                Feral Hog, Wild Pig     No Intervention   \n",
       "7                                             Coyote  Species of Concern   \n",
       "8                                          Gray Wolf          Endangered   \n",
       "9                                           Red Wolf          Endangered   \n",
       "\n",
       "   is_protected  is_sheep  \n",
       "0         False     False  \n",
       "1         False     False  \n",
       "2         False     False  \n",
       "3         False      True  \n",
       "4         False     False  \n",
       "5         False     False  \n",
       "6         False     False  \n",
       "7          True     False  \n",
       "8          True     False  \n",
       "9          True     False  "
      ]
     },
     "execution_count": 100,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "species.head(10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 101,
   "metadata": {},
   "outputs": [],
   "source": [
    "is_sheep = species[species.is_sheep == True]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Select the rows of `species` where `is_sheep` is `True` and examine the results."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 108,
   "metadata": {
    "collapsed": true
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style>\n",
       "    .dataframe thead tr:only-child th {\n",
       "        text-align: right;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: left;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>category</th>\n",
       "      <th>scientific_name</th>\n",
       "      <th>common_names</th>\n",
       "      <th>conservation_status</th>\n",
       "      <th>is_protected</th>\n",
       "      <th>is_sheep</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Mammal</td>\n",
       "      <td>Ovis aries</td>\n",
       "      <td>Domestic Sheep, Mouflon, Red Sheep, Sheep (Feral)</td>\n",
       "      <td>No Intervention</td>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1139</th>\n",
       "      <td>Vascular Plant</td>\n",
       "      <td>Rumex acetosella</td>\n",
       "      <td>Sheep Sorrel, Sheep Sorrell</td>\n",
       "      <td>No Intervention</td>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2233</th>\n",
       "      <td>Vascular Plant</td>\n",
       "      <td>Festuca filiformis</td>\n",
       "      <td>Fineleaf Sheep Fescue</td>\n",
       "      <td>No Intervention</td>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3014</th>\n",
       "      <td>Mammal</td>\n",
       "      <td>Ovis canadensis</td>\n",
       "      <td>Bighorn Sheep, Bighorn Sheep</td>\n",
       "      <td>Species of Concern</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3758</th>\n",
       "      <td>Vascular Plant</td>\n",
       "      <td>Rumex acetosella</td>\n",
       "      <td>Common Sheep Sorrel, Field Sorrel, Red Sorrel,...</td>\n",
       "      <td>No Intervention</td>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3761</th>\n",
       "      <td>Vascular Plant</td>\n",
       "      <td>Rumex paucifolius</td>\n",
       "      <td>Alpine Sheep Sorrel, Fewleaved Dock, Meadow Dock</td>\n",
       "      <td>No Intervention</td>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4091</th>\n",
       "      <td>Vascular Plant</td>\n",
       "      <td>Carex illota</td>\n",
       "      <td>Sheep Sedge, Smallhead Sedge</td>\n",
       "      <td>No Intervention</td>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4383</th>\n",
       "      <td>Vascular Plant</td>\n",
       "      <td>Potentilla ovina var. ovina</td>\n",
       "      <td>Sheep Cinquefoil</td>\n",
       "      <td>No Intervention</td>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4446</th>\n",
       "      <td>Mammal</td>\n",
       "      <td>Ovis canadensis sierrae</td>\n",
       "      <td>Sierra Nevada Bighorn Sheep</td>\n",
       "      <td>Endangered</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "            category              scientific_name  \\\n",
       "3             Mammal                   Ovis aries   \n",
       "1139  Vascular Plant             Rumex acetosella   \n",
       "2233  Vascular Plant           Festuca filiformis   \n",
       "3014          Mammal              Ovis canadensis   \n",
       "3758  Vascular Plant             Rumex acetosella   \n",
       "3761  Vascular Plant            Rumex paucifolius   \n",
       "4091  Vascular Plant                 Carex illota   \n",
       "4383  Vascular Plant  Potentilla ovina var. ovina   \n",
       "4446          Mammal      Ovis canadensis sierrae   \n",
       "\n",
       "                                           common_names conservation_status  \\\n",
       "3     Domestic Sheep, Mouflon, Red Sheep, Sheep (Feral)     No Intervention   \n",
       "1139                        Sheep Sorrel, Sheep Sorrell     No Intervention   \n",
       "2233                              Fineleaf Sheep Fescue     No Intervention   \n",
       "3014                       Bighorn Sheep, Bighorn Sheep  Species of Concern   \n",
       "3758  Common Sheep Sorrel, Field Sorrel, Red Sorrel,...     No Intervention   \n",
       "3761   Alpine Sheep Sorrel, Fewleaved Dock, Meadow Dock     No Intervention   \n",
       "4091                       Sheep Sedge, Smallhead Sedge     No Intervention   \n",
       "4383                                   Sheep Cinquefoil     No Intervention   \n",
       "4446                        Sierra Nevada Bighorn Sheep          Endangered   \n",
       "\n",
       "      is_protected  is_sheep  \n",
       "3            False      True  \n",
       "1139         False      True  \n",
       "2233         False      True  \n",
       "3014          True      True  \n",
       "3758         False      True  \n",
       "3761         False      True  \n",
       "4091         False      True  \n",
       "4383         False      True  \n",
       "4446          True      True  "
      ]
     },
     "execution_count": 108,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "is_sheep.head(10)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Many of the results are actually plants.  Select the rows of `species` where `is_sheep` is `True` and `category` is `Mammal`.  Save the results to the variable `sheep_species`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 105,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "sheep_species = is_sheep[is_sheep.category == 'Mammal']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 109,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style>\n",
       "    .dataframe thead tr:only-child th {\n",
       "        text-align: right;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: left;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>category</th>\n",
       "      <th>scientific_name</th>\n",
       "      <th>common_names</th>\n",
       "      <th>conservation_status</th>\n",
       "      <th>is_protected</th>\n",
       "      <th>is_sheep</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Mammal</td>\n",
       "      <td>Ovis aries</td>\n",
       "      <td>Domestic Sheep, Mouflon, Red Sheep, Sheep (Feral)</td>\n",
       "      <td>No Intervention</td>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3014</th>\n",
       "      <td>Mammal</td>\n",
       "      <td>Ovis canadensis</td>\n",
       "      <td>Bighorn Sheep, Bighorn Sheep</td>\n",
       "      <td>Species of Concern</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4446</th>\n",
       "      <td>Mammal</td>\n",
       "      <td>Ovis canadensis sierrae</td>\n",
       "      <td>Sierra Nevada Bighorn Sheep</td>\n",
       "      <td>Endangered</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     category          scientific_name  \\\n",
       "3      Mammal               Ovis aries   \n",
       "3014   Mammal          Ovis canadensis   \n",
       "4446   Mammal  Ovis canadensis sierrae   \n",
       "\n",
       "                                           common_names conservation_status  \\\n",
       "3     Domestic Sheep, Mouflon, Red Sheep, Sheep (Feral)     No Intervention   \n",
       "3014                       Bighorn Sheep, Bighorn Sheep  Species of Concern   \n",
       "4446                        Sierra Nevada Bighorn Sheep          Endangered   \n",
       "\n",
       "      is_protected  is_sheep  \n",
       "3            False      True  \n",
       "3014          True      True  \n",
       "4446          True      True  "
      ]
     },
     "execution_count": 109,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sheep_species.head(10)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Now merge `sheep_species` with `observations` to get a DataFrame with observations of sheep.  Save this DataFrame as `sheep_observations`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 110,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "sheep_observations = pd.merge(sheep_species, observations)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 116,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style>\n",
       "    .dataframe thead tr:only-child th {\n",
       "        text-align: right;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: left;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>category</th>\n",
       "      <th>scientific_name</th>\n",
       "      <th>common_names</th>\n",
       "      <th>conservation_status</th>\n",
       "      <th>is_protected</th>\n",
       "      <th>is_sheep</th>\n",
       "      <th>park_name</th>\n",
       "      <th>observations</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Mammal</td>\n",
       "      <td>Ovis aries</td>\n",
       "      <td>Domestic Sheep, Mouflon, Red Sheep, Sheep (Feral)</td>\n",
       "      <td>No Intervention</td>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "      <td>Yosemite National Park</td>\n",
       "      <td>126</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Mammal</td>\n",
       "      <td>Ovis aries</td>\n",
       "      <td>Domestic Sheep, Mouflon, Red Sheep, Sheep (Feral)</td>\n",
       "      <td>No Intervention</td>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "      <td>Great Smoky Mountains National Park</td>\n",
       "      <td>76</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Mammal</td>\n",
       "      <td>Ovis aries</td>\n",
       "      <td>Domestic Sheep, Mouflon, Red Sheep, Sheep (Feral)</td>\n",
       "      <td>No Intervention</td>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "      <td>Bryce National Park</td>\n",
       "      <td>119</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Mammal</td>\n",
       "      <td>Ovis aries</td>\n",
       "      <td>Domestic Sheep, Mouflon, Red Sheep, Sheep (Feral)</td>\n",
       "      <td>No Intervention</td>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "      <td>Yellowstone National Park</td>\n",
       "      <td>221</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Mammal</td>\n",
       "      <td>Ovis canadensis</td>\n",
       "      <td>Bighorn Sheep, Bighorn Sheep</td>\n",
       "      <td>Species of Concern</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "      <td>Yellowstone National Park</td>\n",
       "      <td>219</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>Mammal</td>\n",
       "      <td>Ovis canadensis</td>\n",
       "      <td>Bighorn Sheep, Bighorn Sheep</td>\n",
       "      <td>Species of Concern</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "      <td>Bryce National Park</td>\n",
       "      <td>109</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>Mammal</td>\n",
       "      <td>Ovis canadensis</td>\n",
       "      <td>Bighorn Sheep, Bighorn Sheep</td>\n",
       "      <td>Species of Concern</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "      <td>Yosemite National Park</td>\n",
       "      <td>117</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>Mammal</td>\n",
       "      <td>Ovis canadensis</td>\n",
       "      <td>Bighorn Sheep, Bighorn Sheep</td>\n",
       "      <td>Species of Concern</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "      <td>Great Smoky Mountains National Park</td>\n",
       "      <td>48</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>Mammal</td>\n",
       "      <td>Ovis canadensis sierrae</td>\n",
       "      <td>Sierra Nevada Bighorn Sheep</td>\n",
       "      <td>Endangered</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "      <td>Yellowstone National Park</td>\n",
       "      <td>67</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>Mammal</td>\n",
       "      <td>Ovis canadensis sierrae</td>\n",
       "      <td>Sierra Nevada Bighorn Sheep</td>\n",
       "      <td>Endangered</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "      <td>Yosemite National Park</td>\n",
       "      <td>39</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>10</th>\n",
       "      <td>Mammal</td>\n",
       "      <td>Ovis canadensis sierrae</td>\n",
       "      <td>Sierra Nevada Bighorn Sheep</td>\n",
       "      <td>Endangered</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "      <td>Bryce National Park</td>\n",
       "      <td>22</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>11</th>\n",
       "      <td>Mammal</td>\n",
       "      <td>Ovis canadensis sierrae</td>\n",
       "      <td>Sierra Nevada Bighorn Sheep</td>\n",
       "      <td>Endangered</td>\n",
       "      <td>True</td>\n",
       "      <td>True</td>\n",
       "      <td>Great Smoky Mountains National Park</td>\n",
       "      <td>25</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   category          scientific_name  \\\n",
       "0    Mammal               Ovis aries   \n",
       "1    Mammal               Ovis aries   \n",
       "2    Mammal               Ovis aries   \n",
       "3    Mammal               Ovis aries   \n",
       "4    Mammal          Ovis canadensis   \n",
       "5    Mammal          Ovis canadensis   \n",
       "6    Mammal          Ovis canadensis   \n",
       "7    Mammal          Ovis canadensis   \n",
       "8    Mammal  Ovis canadensis sierrae   \n",
       "9    Mammal  Ovis canadensis sierrae   \n",
       "10   Mammal  Ovis canadensis sierrae   \n",
       "11   Mammal  Ovis canadensis sierrae   \n",
       "\n",
       "                                         common_names conservation_status  \\\n",
       "0   Domestic Sheep, Mouflon, Red Sheep, Sheep (Feral)     No Intervention   \n",
       "1   Domestic Sheep, Mouflon, Red Sheep, Sheep (Feral)     No Intervention   \n",
       "2   Domestic Sheep, Mouflon, Red Sheep, Sheep (Feral)     No Intervention   \n",
       "3   Domestic Sheep, Mouflon, Red Sheep, Sheep (Feral)     No Intervention   \n",
       "4                        Bighorn Sheep, Bighorn Sheep  Species of Concern   \n",
       "5                        Bighorn Sheep, Bighorn Sheep  Species of Concern   \n",
       "6                        Bighorn Sheep, Bighorn Sheep  Species of Concern   \n",
       "7                        Bighorn Sheep, Bighorn Sheep  Species of Concern   \n",
       "8                         Sierra Nevada Bighorn Sheep          Endangered   \n",
       "9                         Sierra Nevada Bighorn Sheep          Endangered   \n",
       "10                        Sierra Nevada Bighorn Sheep          Endangered   \n",
       "11                        Sierra Nevada Bighorn Sheep          Endangered   \n",
       "\n",
       "    is_protected  is_sheep                            park_name  observations  \n",
       "0          False      True               Yosemite National Park           126  \n",
       "1          False      True  Great Smoky Mountains National Park            76  \n",
       "2          False      True                  Bryce National Park           119  \n",
       "3          False      True            Yellowstone National Park           221  \n",
       "4           True      True            Yellowstone National Park           219  \n",
       "5           True      True                  Bryce National Park           109  \n",
       "6           True      True               Yosemite National Park           117  \n",
       "7           True      True  Great Smoky Mountains National Park            48  \n",
       "8           True      True            Yellowstone National Park            67  \n",
       "9           True      True               Yosemite National Park            39  \n",
       "10          True      True                  Bryce National Park            22  \n",
       "11          True      True  Great Smoky Mountains National Park            25  "
      ]
     },
     "execution_count": 116,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sheep_observations.head(20)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "How many total sheep observations (across all three species) were made at each national park?  Use `groupby` to get the `sum` of `observations` for each `park_name`.  Save your answer to `obs_by_park`.\n",
    "\n",
    "This is the total number of sheep observed in each park over the past 7 days."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 118,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "obs_by_park = sheep_observations.groupby('park_name').observations.sum().reset_index()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 119,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style>\n",
       "    .dataframe thead tr:only-child th {\n",
       "        text-align: right;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: left;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>park_name</th>\n",
       "      <th>observations</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Bryce National Park</td>\n",
       "      <td>250</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Great Smoky Mountains National Park</td>\n",
       "      <td>149</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Yellowstone National Park</td>\n",
       "      <td>507</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Yosemite National Park</td>\n",
       "      <td>282</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                             park_name  observations\n",
       "0                  Bryce National Park           250\n",
       "1  Great Smoky Mountains National Park           149\n",
       "2            Yellowstone National Park           507\n",
       "3               Yosemite National Park           282"
      ]
     },
     "execution_count": 119,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "obs_by_park.head(10)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Create a bar chart showing the different number of observations per week at each park.\n",
    "\n",
    "1. Start by creating a wide figure with `figsize=(16, 4)`\n",
    "1. Start by creating an axes object called `ax` using `plt.subplot`.\n",
    "2. Create a bar chart whose heights are equal to `observations` column of `obs_by_park`.\n",
    "3. Create an x-tick for each of the bars.\n",
    "4. Label each x-tick with the label from `park_name` in `obs_by_park`\n",
    "5. Label the y-axis `Number of Observations`\n",
    "6. Title the graph `Observations of Sheep per Week`\n",
    "7. Plot the grap using `plt.show()`"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 140,
   "metadata": {
    "collapsed": true
   },
   "outputs": [
    {
     "data": {
      "image/png": "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\nI2moNbZVdU17vgH4Hl3T4uuTrAnQnm9oo18DrNubfJ1WNn6eB1fV5lW1+Zw5c4YZviRJkiRpBAwt\nsU3yyCQrjA0DLwTOB44Edmuj7QYc0YaPBHZNsmySDYANgdOGFZ8kSZIkafEwzKbIawDfSzK2nK9X\n1dFJTgcOS/IGYB6wM0BVXZDkMOBC4G5gL3tEliRJkiRNZ2iJbVVdDmw6QfnNwLaTTHMAcMCwYpIk\nSZIkLX5m4+9+JEmSJElaYExsJUmSJEkjzcRWkiRJkjTSTGwlSZIkSSPNxFaSJEmSNNJMbCVJkiRJ\nI83EVpIkSZI00kxsJUmSJEkjzcRWkiRJkjTSTGwlSZIkSSPNxFaSJEmSNNJMbCVJkiRJI83EVpIk\nSZI00kxsJUmSJEkjzcRWkiRJkjTSTGwlSZIkSSPNxFaSJEmSNNJMbCVJkiRJI83EVpIkSZI00kxs\nJUmSJEkjzcRWkiRJkjTSTGwlSZIkSSPNxFaSJEmSNNJMbCVJkiRJI83EVpIkSZI00kxsJUmSJEkj\nzcRWkiRJkjTSTGwlSZIkSSPNxFaSJEmSNNJMbCVJkiRJI83EVpIkSZI00maU2CZZJcmThhWMJEmS\nJEkzNW1im+SEJCsmWRU4C/h8koMGXUCSpZOcneSo9nrVJMckubQ9r9Ibd78klyW5JMmL5meFJEmS\nJElLlkFqbFeqqluBVwBfqaqnA8+fwTL2Bi7qvd4XOK6qNgSOa69JshGwK7AxsB3w6SRLz2A5kiRJ\nkqQl0CCJ7TJJ1gR2Bo6aycyTrAO8BPhCr3hH4JA2fAjw8l75oVV1Z1VdAVwGPG0my5MkSZIkLXkG\nSWzfD/wYuKyqTk/yGODSAef/n8A7gHt7ZWtU1bVt+DpgjTa8NnBVb7yrW9kDJNkzyRlJzrjxxhsH\nDEOSJEmStLiaNrGtqm9V1ZOq6o3t9eVV9TfTTZfkpcANVXXmFPMuoGYScFUdXFWbV9Xmc+bMmcmk\nkiRJkqTF0DLTjZBkDvD3wNz++FX1+mkmfRbwsiQvBpYDVkzyv8D1SdasqmtbE+cb2vjXAOv2pl+n\nlUmSJEmSNKlBmiIfAawEHAv8oPeYUlXtV1XrVNVcuk6hflpVrwaOBHZro+3W5k8r3zXJskk2ADYE\nTpvBukiSJEmSlkDT1tgCj6iqdy7AZR4IHJbkDcA8uk6pqKoLkhwGXAjcDexVVfcswOVKkiRJkhZD\n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\nNBNbSZIkSdJIM7GVJEmSJI00E1tJkiRJ0kgzsZUkSZIkjTQTW0mSJEnSSDOxlSRJkiSNNBNbSZIk\nSdJIM7GVJEmSJI00E1tJkiRJ0kgzsZUkSZIkjTQTW0mSJEnSSDOxlSRJkiSNNBNbSZIkSdJIM7GV\nJEmSJI00E1tJkiRJ0kgzsZUkSZIkjTQTW0mSJEnSSDOxlSRJkiSNNBNbSZIkSdJIM7GVJEmSJI20\nRS6xTbJdkkuSXJZk39mOR5IkSZK0aFukEtskSwOfArYHNgJemWSj2Y1KkiRJkrQoW6QSW+BpwGVV\ndXlV3QUcCuw4yzFJkiRJkhZhqarZjuE+Sf4W2K6q9mivXwM8vare1BtnT2DP9vIJwCULPVDNttWB\nm2Y7CGkx43ElLXgeV9KC5TG1ZFq/quZMN9IyCyOSBamqDgYOnu04NHuSnFFVm892HNLixONKWvA8\nrqQFy2NKU1nUmiJfA6zbe71OK5MkSZIkaUKLWmJ7OrBhkg2SPBzYFThylmOSJEmSJC3CFqmmyFV1\nd5I3AT8Glga+VFUXzHJYWvTYFF1a8DyupAXP40pasDymNKlFqvMoSZIkSZJmalFriixJkiRJ0oyY\n2EqSJEmSRpqJ7RIoyT1JfpnknCRnJXnmQlz27knuTfKkXtn5SeZOM90+SR7Re/3DJCsv4Nj2T/Iv\nk5Rf07bZ+UleNsP57p7kkwsu0sVbkjWSfD3J5UnOTPLzJH+9AOf/rinee32S85Kc2z7rHRfA8uYm\nOX8+p906SSXZo1e2WSt70L76UE21bcaN95CPv9667dArOyrJ1tNMt3uStXqvv5Bko4cSyyTLeNAx\n28pvbN8FFyb5+xnOd+skRy24SBdt6ZySZPte2U5Jjp5imquTrJxkmSS3DCmutyZZbhjz7i3j+W3/\n7q/70Um2mma61yf5i97r/0nyhAUc2x5J/nOS8rH9+6Ikr5/hfJ+f5PAFF6lmYn6OtyHEsHSSk9vw\nY5LsOsPpl2nHzYd7Zfsmefc0022TZMve672SvGqm8U+zjMcl+eUk5Xf0fhc+lSQzmO/QvuuWRCa2\nS6Y7qmqzqtoU2A/40PgRkgyzY7GrgX+d4TT7APcltlX14qpamF8E/1FVmwE7AV9KMtCxM+TtuNhp\nPwaHAydV1WOq6ql0vaOvM8G487ttJ0zekqxDt19uVVVPArYEzp3PZSxI5wM7916/EjhnSMsaKLFd\n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\n",
      "text/plain": [
       "<matplotlib.figure.Figure at 0x1216472b0>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.figure(figsize=(16,4))\n",
    "ax = plt.subplot()\n",
    "plt.bar(range(len(obs_by_park)),obs_by_park.observations.values)\n",
    "ax.set_xticks(range(len(obs_by_park.park_name)))\n",
    "ax.set_xticklabels(obs_by_park.park_name)\n",
    "ax.set_ylabel('Number of Observations')\n",
    "ax.set_title('Observations of Sheep per Week')\n",
    "plt.savefig('obs_sheep_weekly.png')\n",
    "\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Our scientists know that 15% of sheep at Bryce National Park have foot and mouth disease.  Park rangers at Yellowstone National Park have been running a program to reduce the rate of foot and mouth disease at that park.  The scientists want to test whether or not this program is working.  They want to be able to detect reductions of at least 5 percentage point.  For instance, if 10% of sheep in Yellowstone have foot and mouth disease, they'd like to be able to know this, with confidence.\n",
    "\n",
    "Use the sample size calculator at <a href=\"https://www.optimizely.com/sample-size-calculator/\">Optimizely</a> to calculate the number of sheep that they would need to observe from each park.  Use the default level of significance (90%).\n",
    "\n",
    "Remember that \"Minimum Detectable Effect\" is a percent of the baseline."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 129,
   "metadata": {
    "collapsed": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "33.333333333333336\n"
     ]
    }
   ],
   "source": [
    "minimum_detectable_effect = 100 * 0.05 / 0.15\n",
    "print(minimum_detectable_effect)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 130,
   "metadata": {},
   "outputs": [],
   "source": [
    "sample_size = 510"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "How many weeks would you need to observe sheep at Bryce National Park in order to observe enough sheep?  How many weeks would you need to observe at Yellowstone National Park to observe enough sheep?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 133,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "bryce = sample_size/250\n",
    "yellowstone = sample_size/507"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 138,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Weeks you'd need to observe sheep at Bryce: 2.04\n",
      "Weeks you'd need to observe sheep at Yellowstone: 1.0059171597633136\n"
     ]
    }
   ],
   "source": [
    "print('Weeks you\\'d need to observe sheep at Bryce:', bryce)\n",
    "print('Weeks you\\'d need to observe sheep at Yellowstone:', yellowstone)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [default]",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.5.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
