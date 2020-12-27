# https://stackoverflow.com/questions/47730785/parsing-a-file-by-blocks-and-extracting-information-from-each-of-the-blocks-with
# 讀取 Solvespace 轉出的 wrl 檔案
'''
dart
https://github.com/google/quiver-dart
meshlabserver.exe -i <wrl file> -o <x3d file>
'''
import itertools
import json
import logging
from pprint import pprint
import os

# For the next line, use logging.WARN to turn off debug print, use
# logging.DEBUG to turn on
logging.basicConfig(level=os.getenv('LOGLEVEL', logging.WARN))
logger = logging.getLogger(__name__)


def skip_pass(marker, lines):
    """
    Skip until reach the line which contains the marker, then also skip
    the marker line
    """
    result = itertools.dropwhile(
        lambda line: marker not in line,  # Condition
        lines)                            # The lines
    next(result)                          # skip pass the marker
    return result

def take(marker, lines):
    """
    Take and return those lines which contains a marker
    """
    result = itertools.takewhile(
        lambda line: marker in line,      # Condition
        lines)                            # The lines
    return result

def parse_indexed_face_set(translate, lines):
    """
    Parse one block of 'geometry IndexedFaceSet'
    """
    # lines = skip_pass('geometry IndexedFaceSet', lines)

    # Parse the "point" structure
    lines = skip_pass('point', lines)
    point_lines = take(',', lines)
    verts = [[float(token) for token in line.strip(',\n').split()] for line in point_lines]
    logger.debug('verts: %r', verts)

    # parse the coordIndex structure
    lines = skip_pass('coordIndex', lines)
    coor_lines = take(',', lines)
    coord_index = [tuple(int(token) for token in line.strip(',\n').split(',')) for line in coor_lines]
    logger.debug('coord_index: %r', coord_index)

    facets = [[verts[i] for i in indices[:3]] for indices in coord_index]
    logger.debug('facets: %r', facets)

    return dict(vert=verts, facets=facets, translate=translate, normals=[])

def parse_translate(line):
    """
    Given a line such as: "translate 5 6 7", return [5.0, 6.0, 7.0]
    """
    translate = [float(x) for x in line.split()[1:4]]
    return translate

def extractDataFromVRML(root):
    indexed_face_sets = []
    translate = []
    with open(root + '.wrl') as infile:
        for line in infile:
            if 'geometry IndexedFaceSet' in line:
                a_set = parse_indexed_face_set(translate=translate, lines=infile)
                indexed_face_sets.append(a_set)
            elif 'translation' in line and line.split()[0] == 'translation':
                translate = parse_translate(line)

    return indexed_face_sets


# main
indexed_face_sets = extractDataFromVRML('base')
# 或可從 indexed_face_sets 中切出不同零件的點與三角形, 然後存成一個 wrl
# 以便輸入 Webots
for a_set in indexed_face_sets:
    # 列出所有點資料
    print('vert:', a_set['vert'])
    # 列出所有三角形資料
    print('facets:', a_set['facets'])
    print('---')