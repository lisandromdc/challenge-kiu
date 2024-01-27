import { helpers } from '@/helpers/helpers.js'

export class Show {
  image = '';
  name = '';
  type = '';
  network = '';
  officialSite = '';
  genres = [];

  constructor(params) {
    if (params.image) this.image = params.image.original;
    this.name = params.name;
    this.type = params.type;
    if (params.network) this.network = params.network.name;
    this.officialSite = params.officialSite;
    this.genres = params.genres;
  }
  
  static sort(shows) {
    return shows.sort((a, b) => {
      // sort by vowels quantity
      const vowelsQuantityA = helpers.getVowelsQuantity(a.name);
      const vowelsQuantityB = helpers.getVowelsQuantity(b.name);
      if (vowelsQuantityA < vowelsQuantityB) return -1;
      if (vowelsQuantityA > vowelsQuantityB) return 1;
      // sort by alphabet
      return a.name.localeCompare(b.name);
    });
  }
}