# pycomicvine
A python wrapper for comicvine.com

## Build status
[![Build Status](https://travis-ci.org/authmillenon/pycomicvine.png?branch=master)](https://travis-ci.org/authmillenon/pycomicvine)

## Installation
Using setuptools you can install *pycomicvine* as follows:

    python setup.py install

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
the [API](https://www.comicvine.com/api/documentation#toc-0-3):

<table>
<thead>
<tr class="header">
<th align="left">Class</th>
<th align="left">API resource</th>
<th align="left">resource type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left">Character</td>
<td align="left">/character</td>
<td align="left">singular resource</td>
</tr>
<tr class="even">
<td align="left">Characters</td>
<td align="left">/characters</td>
<td align="left">list resource</td>
</tr>
<tr class="odd">
<td align="left">Chat</td>
<td align="left">/chat</td>
<td align="left">singular resource</td>
</tr>
<tr class="even">
<td align="left">Chats</td>
<td align="left">/chats</td>
<td align="left">list resource</td>
</tr>
<tr class="odd">
<td align="left">Concept</td>
<td align="left">/concept</td>
<td align="left">singular resource</td>
</tr>
<tr class="even">
<td align="left">Concepts</td>
<td align="left">/concepts</td>
<td align="left">list resource</td>
</tr>
<tr class="odd">
<td align="left">Issue</td>
<td align="left">/issue</td>
<td align="left">singular resource</td>
</tr>
<tr class="even">
<td align="left">Issues</td>
<td align="left">/issues</td>
<td align="left">list resource</td>
</tr>
<tr class="odd">
<td align="left">Location</td>
<td align="left">/location</td>
<td align="left">singular resource</td>
</tr>
<tr class="even">
<td align="left">Locations</td>
<td align="left">/locations</td>
<td align="left">list resource</td>
</tr>
<tr class="odd">
<td align="left">Movie</td>
<td align="left">/movie</td>
<td align="left">singular resource</td>
</tr>
<tr class="even">
<td align="left">Movies</td>
<td align="left">/movies</td>
<td align="left">list resource</td>
</tr>
<tr class="odd">
<td align="left">Object</td>
<td align="left">/object</td>
<td align="left">singular resource</td>
</tr>
<tr class="even">
<td align="left">Objects</td>
<td align="left">/objects</td>
<td align="left">list resource</td>
</tr>
<tr class="odd">
<td align="left">Origin</td>
<td align="left">/origin</td>
<td align="left">singular resource</td>
</tr>
<tr class="even">
<td align="left">Origins</td>
<td align="left">/origins</td>
<td align="left">list resource</td>
</tr>
<tr class="odd">
<td align="left">Person</td>
<td align="left">/person</td>
<td align="left">singular resource</td>
</tr>
<tr class="even">
<td align="left">People</td>
<td align="left">/people</td>
<td align="left">list resource</td>
</tr>
<tr class="odd">
<td align="left">Power</td>
<td align="left">/power</td>
<td align="left">singular resource</td>
</tr>
<tr class="even">
<td align="left">Powers</td>
<td align="left">/powers</td>
<td align="left">list resource</td>
</tr>
<tr class="odd">
<td align="left">Promo</td>
<td align="left">/promo</td>
<td align="left">singular resource</td>
</tr>
<tr class="even">
<td align="left">Promos</td>
<td align="left">/promos</td>
<td align="left">list resource</td>
</tr>
<tr class="odd">
<td align="left">Publisher</td>
<td align="left">/publisher</td>
<td align="left">singular resource</td>
</tr>
<tr class="even">
<td align="left">Publishers</td>
<td align="left">/publishers</td>
<td align="left">list resource</td>
</tr>
<tr class="odd">
<td align="left">Search</td>
<td align="left">/search</td>
<td align="left">list resource</td>
</tr>
<tr class="even">
<td align="left">StoryArc</td>
<td align="left">/story_arc</td>
<td align="left">singular resource</td>
</tr>
<tr class="odd">
<td align="left">StoryArcs</td>
<td align="left">/story_arcs</td>
<td align="left">list resource</td>
</tr>
<tr class="even">
<td align="left">Team</td>
<td align="left">/team</td>
<td align="left">singular resource</td>
</tr>
<tr class="odd">
<td align="left">Teams</td>
<td align="left">/teams</td>
<td align="left">list resource</td>
</tr>
<tr class="even">
<td align="left">Types</td>
<td align="left">/types</td>
<td align="left">list resource</td>
</tr>
<tr class="odd">
<td align="left">Video</td>
<td align="left">/video</td>
<td align="left">singular resource</td>
</tr>
<tr class="even">
<td align="left">Videos</td>
<td align="left">/videos</td>
<td align="left">list resource</td>
</tr>
<tr class="odd">
<td align="left">VideoType</td>
<td align="left">/video_type</td>
<td align="left">singular resource</td>
</tr>
<tr class="even">
<td align="left">VideoTypes</td>
<td align="left">/video_types</td>
<td align="left">list resource</td>
</tr>
<tr class="odd">
<td align="left">Volume</td>
<td align="left">/volume</td>
<td align="left">singular resource</td>
</tr>
<tr class="even">
<td align="left">Volumes</td>
<td align="left">/volumes</td>
<td align="left">list resource</td>
</tr>
</tbody>
</table>

## Contribute
You can contribute by submitting issue tickets here on GitHub, 
including Pull Requests. You can test *pycomicvine* by calling

    python setup.py test

## License
Copyright (c) 2013 Martin Lenders

Permission is hereby granted, free of charge, to any person obtaining 
a copy of this software and associated documentation files (the 
"Software"), to deal in the Software without restriction, including 
without limitation the rights to use, copy, modify, merge, publish, 
distribute, sublicense, and/or sell copies of the Software, and to 
permit persons to whom the Software is furnished to do so, subject to 
the following conditions:

The above copyright notice and this permission notice shall be 
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, 
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF 
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND 
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS 
BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN 
ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN 
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE 
SOFTWARE.
