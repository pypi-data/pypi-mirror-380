# Copyright 2024 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""CLI entrypoint for generating creative map."""

# pylint: disable=C0330, g-bad-import-order, g-multiple-import

import argparse
import sys
from typing import get_args

import media_fetching
import media_similarity
import media_tagging
from garf_executors.entrypoints import utils as garf_utils
from media_tagging import media

import filonov
from filonov.entrypoints import utils

AVAILABLE_TAGGERS = list(media_tagging.taggers.TAGGERS.keys())


def main():  # noqa: D103
  parser = argparse.ArgumentParser()
  parser.add_argument(
    '--source',
    dest='source',
    choices=get_args(media_fetching.sources.models.InputSource),
    default='googleads',
    help='Which datasources to use for generating a map',
  )
  parser.add_argument(
    '--media-type',
    dest='media_type',
    choices=media.MediaTypeEnum.options(),
    help='Type of media.',
  )
  parser.add_argument(
    '--tagger',
    dest='tagger',
    choices=AVAILABLE_TAGGERS,
    default=None,
    help='Type of tagger',
  )
  parser.add_argument(
    '--size-base',
    dest='size_base',
    help='Metric to base node sizes on',
  )
  parser.add_argument(
    '--db-uri',
    dest='db_uri',
    help='Database connection string to store and retrieve results',
  )
  parser.add_argument(
    '--output-name',
    dest='output_name',
    default='creative_map',
    help='Name of output file',
  )
  parser.add_argument(
    '--trim-tags-threshold',
    dest='trim_tags_threshold',
    default=None,
    type=float,
    help='Min allowed score for tags',
  )
  parser.add_argument(
    '--parallel-threshold',
    dest='parallel_threshold',
    default=10,
    type=int,
    help='Number of parallel processes to perform media tagging',
  )
  parser.add_argument(
    '--loglevel',
    dest='loglevel',
    default='INFO',
    help='Log level',
  )
  parser.add_argument(
    '--logger',
    dest='logger',
    default='rich',
    choices=['local', 'rich'],
    help='Type of logger',
  )
  parser.add_argument('-v', '--version', dest='version', action='store_true')
  args, kwargs = parser.parse_known_args()

  if args.version:
    print(f'filonov version: {filonov.__version__}')
    sys.exit()

  _ = garf_utils.init_logging(loglevel=args.loglevel, logger_type=args.logger)
  supported_enrichers = (
    media_fetching.enrichers.enricher.AVAILABLE_MODULES.keys()
  )
  parsed_param_keys = set(
    [args.source, 'tagger', 'similarity'] + list(supported_enrichers)
  )
  extra_parameters = garf_utils.ParamsParser(parsed_param_keys).parse(kwargs)
  fetching_service = media_fetching.MediaFetchingService(args.source)
  tagging_service = media_tagging.MediaTaggingService(
    tagging_results_repository=(
      media_tagging.repositories.SqlAlchemyTaggingResultsRepository(args.db_uri)
    )
  )
  similarity_service = media_similarity.MediaSimilarityService(
    media_similarity.repositories.SqlAlchemySimilarityPairsRepository(
      args.db_uri
    )
  )
  tagger = args.tagger
  media_type = args.media_type
  if args.source == 'youtube':
    media_type = 'YOUTUBE_VIDEO'
    tagger = 'gemini'
  request = filonov.CreativeMapGenerateRequest(
    source=args.source,
    media_type=media_type,
    tagger=tagger,
    tagger_parameters=extra_parameters.get('tagger'),
    similarity_parameters=extra_parameters.get('similarity'),
    source_parameters=extra_parameters.get(args.source),
    output_parameters=filonov.filonov_service.OutputParameters(
      output_name=args.output_name
    ),
    parallel_threshold=args.parallel_threshold,
    trim_tags_threshold=args.trim_tags_threshold,
    context=extra_parameters,
  )
  filonov_service = filonov.FilonovService(
    fetching_service, tagging_service, similarity_service
  )
  generated_map = filonov_service.generate_creative_map(request)
  destination = utils.build_creative_map_destination(
    request.output_parameters.output_name
  )
  generated_map.save(destination)


if __name__ == '__main__':
  main()
