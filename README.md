# pycomicvine
A python wrapper for comicvine.com

## Build status
[![Build Status](https://travis-ci.org/authmillenon/pycomicvine.png?branch=master)](https://travis-ci.org/authmillenon/pycomicvine)

## Installation
Using setuptools you can install *pycomicvine* as follows:

    python setup.py

Dependencies:

 * simplejson
 * python-dateutil

## Usage
You can search for resources on comicvine.com.

```python
>>> import pycomicvine
>>> pycomicvine.api_key = "<Your API key>"
>>> pycomicvine.Volume.search("The Walking Dead")
<Volume: The Walking Dead [18166]>
```


Paramaters are identical to the filters stated in the 
[API Documentation](https://www.comicvine.com/api/documentation#toc-0-26),
where ```resources``` is omitted. ```query``` is mandatory and the 
first parameter. ```field_list``` can be either a list of string or
a comma-seperated string.

You can also search mixed resource lists with

```python
>>> pycomicvine.Search("Avengers", field_list=['name','id'])
[<Team: Avengers [3806]>,<Volume: Avengers [7084]>,<Volume: Avengers [33227]>]
```

Again: all parameters match up with the 
[API Documentation](https://www.comicvine.com/api/documentation#toc-0-26). 
As you may have guessed ```Team.search("Teen Titans")``` is equivalent
to ```Search("Teen Titans", resource="team")```.

A list of resources of one type can be downloaded using 

```python
>>> pycomicvine.Objects(filter="name:Mjolnir")
Objects[<Object: Mjolnir [40971]>,<Object: MJOLNIR Powered Assault Armor [56824]>]
```

If you know the ID of a resource you can download it directly:

```python
>>> pycomicvine.Character(20096, all=True)
<Character: Buffy [20096]>
```

The additional parameter ```all``` assures that all fields of the
resource are downloaded. Per default only the ids of resources (and 
fields that might be via ```field_list```) are downloaded. If a field
is not downloaded yet it will be downloaded when it is called.

```python
>>> issue = pycomicvine.Issue(194796)
>>> issue
<Issue: [194796]>
>>> issue.name
'Monster, Part Two'
>>> issue.volume
<Volume: Star Wars: Legacy [18575]>
>>> issue
<Issue: Monster, Part Two [194796]>
```

The additional parameter ```do_not_download``` causes, that nothing is
downloaded on initialisation, even if you give a ```field_list```.
```do_not_download``` is stronger than ```all```

```python
>>> movie = pycomicvine.Movie(108, all=True, field_list=['name'], do_not_download=True)
>>> movie
<Movie: [108]>
>>> movie.name
'Star Trek'
>>> movie
<Movie: Star Trek [108]>
```

Here is a mapping of which class is representing which resource type of 
the (API)[https://www.comicvine.com/api/documentation#toc-0-3]:

Class           API resource    resource type
--------------  --------------  -----------------
Character       /character      singular resource
Characters      /characters     list resource
Chat            /chat           singular resource
Chats           /chats          list resource
Concept         /concept        singular resource
Concepts        /concepts       list resource
Issue           /issue          singular resource
Issues          /issues         list resource
Location        /location       singular resource
Locations       /locations      list resource
Movie           /movie          singular resource
Movies          /movies         list resource
Object          /object         singular resource
Objects         /objects        list resource
Origin          /origin         singular resource
Origins         /origins        list resource
Person          /person         singular resource
Persons         /persons        list resource
Power           /power          singular resource
Powers          /powers         list resource
Promo           /promo          singular resource
Promos          /promos         list resource
Publisher       /publisher      singular resource
Publishers      /publishers     list resource
Search          /search         list resource
StoryArc        /story_arc      singular resource
StoryArcs       /story_arcs     list resource
Team            /team           singular resource
Teams           /teams          list resource
Types           /types          list resource
Video           /video          singular resource
Videos          /videos         list resource
VideoType       /video_type     singular resource
VideoTypes      /video_types    list resource
Volume          /volume         singular resource
Volumes         /volumes        list resource
