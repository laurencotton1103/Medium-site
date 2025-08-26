# the purpose of this file is to read the RSS feed from medium and prepare it for the react application
import feedparser
d = feedparser.parse('https://medium.com/feed/@laurencotton')
d['feed']['title']
