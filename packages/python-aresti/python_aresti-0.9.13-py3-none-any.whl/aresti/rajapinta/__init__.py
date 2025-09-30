from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass
from functools import cached_property
from typing import Any, Iterable, Union

from .hahmo import Hahmo
from ..yhteys import AsynkroninenYhteys
from ..sanoma import RestSanoma
from ..tyokalut import ei_syotetty, luokkamaare, Valinnainen


class RajapintaMeta(type):
  '''
  Lisätään rajapintaluokan määrittelevään luokkaan välimuistitettu,
  oliokohtainen määre oletuksena samalla nimellä, pienin kirjaimin.

  Nimen voi vaihtaa antamalla luokalle määreen `oliomaare`.

  Jos oletetaan seuraavat määrittelyt:

  class YhteysX(AsynkroninenYhteys):
    class RajapintaX(Rajapinta):
      pass
    class RajapintaY(Rajapinta, oliomaare='r_y'):
      pass

  on voimassa:
  - YhteysX.RajapintaX: `RajapintaX` itse;
  - (yhteysX := YhteysX(...)).rajapintax: olio `RajapintaX(yhteys=yhteysX)`;
  - (yhteysX := YhteysX(...)).r_y: olio `RajapintaY(yhteys=yhteysX)`.
  '''

  def __new__(mcs, name, bases, attrs, *, oliomaare=None, **kwargs):
    # pylint: disable=protected-access
    cls = super().__new__(mcs, name, bases, attrs, **kwargs)
    cls.__oliomaare = oliomaare
    return cls
    # def __new__

  def __set_name__(cls, owner, name):
    setattr(
      owner,
      _name := cls.__oliomaare or name.lower(),
      _cls := cached_property(cls)
    )
    _cls.__set_name__(owner, _name)

  # class RajapintaMeta


@dataclass
class Rajapinta(metaclass=RajapintaMeta):

  yhteys: AsynkroninenYhteys

  class ToimintoEiSallittu(RuntimeError):
    pass

  @dataclass
  class Syote(RestSanoma):
    ''' Lähtevän datan tietorakenne. '''

  @luokkamaare
  def Paivitys(cls):
    '''
    Tietorakenne olemassaolevan tietueen päivittämiseen.

    Oletuksena käytetään samaa Syötettä kuin uudelle tietueelle.
    '''
    # pylint: disable=invalid-name
    return cls.Syote
    # def Paivitys

  @dataclass(kw_only=True)
  class Tuloste(RestSanoma):
    ''' Saapuvan datan tietorakenne. '''

  @dataclass(kw_only=True)
  class Hahmo(Hahmo):
    ''' Sijaishahmo tietueiden käsittelyyn rajapinnassa. '''

  class Meta:
    ''' Rajapinnan metatiedot. '''
    # Tiedonvaihtoon käytetty URL, esim. /api/kioski/
    rajapinta: str

    # Tietuekohtaiseen tiedonvaihtoon käytetty URL,
    # oletuksena {rajapinta}/%(pk)s.
    rajapinta_pk: Valinnainen[str] = ei_syotetty

    # Primääriavain tietueen kentissä,
    pk: str = 'id'

    # class Meta

  def __aiter__(self):
    ''' Tuota kaikki tulokset asynkronisesti. '''
    return aiter(self.Hahmo(rajapinta=self))
    # def __call__

  def __call__(
    self,
    tietue: Valinnainen[RestSanoma] = ei_syotetty,
    *,
    pk: Valinnainen[Any] = ei_syotetty,
    **kwargs
  ):
    ''' Muodosta sijaishahmo annetuilla avaimilla. '''
    if tietue is not ei_syotetty and pk is ei_syotetty:
      pk = getattr(tietue, self.Meta.pk, ei_syotetty)
    return self.Hahmo(
      rajapinta=self,
      tietue=tietue,
      pk=pk,
      kwargs=kwargs
    )
    # def __call__

  def _tulkitse_saapuva(self, saapuva) -> Tuloste:
    ''' Tulkitse saapuvan datan sisältämä sanoma. '''
    if not isinstance(saapuva, Mapping):
      raise TypeError(
        f'Noudettu data ei ole kuvaus: {type(saapuva)!r}!'
      )
    return self.Tuloste.saapuva(saapuva)
    # def _tulkitse_saapuva

  def _tulkitse_lahteva(self, lahteva: Syote | Paivitys) -> dict:
    ''' Muodosta lähtevä data sanomalle. '''
    return lahteva.lahteva()
    # def _tulkitse_lahteva

  async def nouda_rajapinnasta(
    self,
    pk: Valinnainen[Union[str, int]] = ei_syotetty,
    **params,
  ) -> list[Tuloste]:
    if pk is not ei_syotetty:
      assert self.Meta.rajapinta_pk
      rajapinta = self.Meta.rajapinta_pk % {'pk': pk}
    else:
      rajapinta = self.Meta.rajapinta
    return await self.yhteys.nouda_data(rajapinta, params=params)
    # async def nouda_rajapinnasta

  async def nouda(self, **params) -> Valinnainen[
    Union[Tuloste, list[Tuloste]]
  ]:
    data = await self.nouda_rajapinnasta(**params)
    if data is None:
      return ei_syotetty
    elif isinstance(data, Mapping):
      return self._tulkitse_saapuva(data)
    elif isinstance(data, Iterable):
      return [self._tulkitse_saapuva(d) for d in data]
    else:
      raise TypeError(
        f'Paluusanoman sisältö on tuntematonta tyyppiä: {data!r}'
      )
    # async def nouda

  async def otsakkeet(self, **params):
    return await self.yhteys.nouda_otsakkeet(
      self.Meta.rajapinta,
      params=params,
    )
    # async def otsakkeet

  async def meta(self, **params):
    return await self.yhteys.nouda_meta(
      self.Meta.rajapinta,
      params=params,
    )
    # async def meta

  async def lisaa(
    self,
    data: Valinnainen[Syote | Iterable[Syote]] = ei_syotetty,
    **kwargs
  ):
    if data is not ei_syotetty and kwargs:
      raise ValueError(
        'Anna joko syöte tai `kwargs`.'
      )
    elif kwargs:
      data = self.Syote(**kwargs)
    elif data is ei_syotetty:
      pass
    elif not isinstance(data, RestSanoma) and isinstance(data, Iterable):
      return [await self.lisaa(alkio) for alkio in data]
    elif not isinstance(data, RestSanoma):
      raise TypeError(f'not isinstance({data!r}, RestSanoma)')
    return self._tulkitse_saapuva(
      await self.yhteys.lisaa_data(
        self.Meta.rajapinta,
        self._tulkitse_lahteva(data) if data is not ei_syotetty else {}
      )
    )
    # async def lisaa

  async def muuta(
    self,
    pk: Union[str, int],
    data: Valinnainen[Paivitys] = ei_syotetty,
    **kwargs
  ):
    assert self.Meta.rajapinta_pk
    if data is not ei_syotetty and kwargs:
      raise ValueError(
        'Anna joko syöte tai `kwargs`.'
      )
    elif kwargs:
      data = self.Paivitys(**kwargs)
    elif data is ei_syotetty:
      pass
    elif not isinstance(data, RestSanoma):
      raise TypeError(f'not isinstance({data!r}, RestSanoma)')
    return self._tulkitse_saapuva(
      await self.yhteys.muuta_data(
        self.Meta.rajapinta_pk % {'pk': pk},
        self._tulkitse_lahteva(data) if data is not ei_syotetty else {}
      )
    )
    # async def muuta

  async def tuhoa(
    self,
    pk: Union[str, int],
  ):
    assert self.Meta.rajapinta_pk
    return self._tulkitse_saapuva(
      await self.yhteys.tuhoa_data(
        self.Meta.rajapinta_pk % {'pk': pk},
      )
    )
    # async def tuhoa

  # class Rajapinta
