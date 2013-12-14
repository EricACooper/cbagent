from cbagent.collectors import Collector


class NSServer(Collector):

    COLLECTOR = "ns_server"

    def _get_stats_uri(self):
        for bucket, stats in self.get_buckets(with_stats=True):
            uri = stats["uri"]
            yield uri, bucket, None  # cluster wide

            stats_list = self.get_http(path=stats["nodeStatsListURI"])
            for server in stats_list["servers"]:
                host = server["hostname"].split(":")[0]
                uri = server["stats"]["uri"]
                yield uri, bucket, host  # server specific

    def _get_stats(self, uri):
        samples = self.get_http(path=uri)  # get last minute samples
        stats = dict()
        for metric, values in samples['op']['samples'].iteritems():
            metric = metric.replace('/', '_')
            stats[metric] = values[-1]  # only the most recent sample
        return stats

    def sample(self):
        for uri, bucket, host in self._get_stats_uri():
            stats = self._get_stats(uri)
            self.store.append(stats, self.cluster, host, bucket, self.COLLECTOR)

    def _get_metrics(self):
        nodes = list(self.get_nodes())
        for bucket, stats in self.get_buckets(with_stats=True):
            stats_directory = self.get_http(path=stats["directoryURI"])
            for block in stats_directory["blocks"]:
                for metric in block["stats"]:
                    yield metric["name"], bucket, None
                    for node in nodes:
                        yield metric["name"], bucket, node

    def update_metadata(self):
        self.mc.add_cluster()

        for bucket in self.get_buckets():
            self.mc.add_bucket(bucket)

        for node in self.get_nodes():
            self.mc.add_server(node)

        for metric, bucket, node in self._get_metrics():
            metric = metric.replace('/', '_')
            self.mc.add_metric(metric, bucket=bucket, server=node,
                               collector=self.COLLECTOR)
